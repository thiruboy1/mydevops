#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
from datetime import datetime

JPG_SIGNATURE = [0xff, 0xd8, 0xff, 0xe0, 0x00, 0x10, 0x4a, 0x46, 0x49, 0x46]


def about():
	print 'Swf extractor. Version 1.0'
	print 'usage: swf-extract <filename.swf> [outdir]' 

# Parse output from swfextract
def parseSwfExtractOutLine(line, template, array):
	pos = line.find(template)
	if pos >= 0:
		s = line[pos+len(template):]
		idss = s.split(',')
		for ids in idss:
			s = ids.strip()
			if s.find('-') > 0:
				s2 = s.split('-')
				i1 = int(s2[0])
				i2 = int(s2[1])
				for i in range(i1, i2+1):
					array.append(i)
			elif len(s) > 0:
				i = int(s)
				array.append(i)
		return True
	return False


# Extract swf resource
def extractSwf(array, srcName, dirName, prefixName, ext, arg):
	for i in array:
		fileName = prefixName + str(i) + '.' + ext
		outName = os.path.join(dirName, fileName)
		os.system('swfextract ' + srcName + ' -o ' + outName + ' -i ' + str(i))
		swfDump(outName)


# save integer array into file
def saveToFile(fileName, data, offset):
	if os.path.exists(fileName):
		print 'file already exists:', fileName
		return
	f = open(fileName, 'wb+')
	pos = 0;
	for b in data:
		if pos >= offset:
			f.write(chr(b))
		pos += 1
	f.close()


# return offset of signature in buffer, or -1 it signature hasn't been found
def findSignatureInBuffer(buf, sign):
	sl = len(sign)
	if sl == 0:
		return 0
	bl = len(buf)
	bi = 0
	si = 0
	pos_bi_save = 0
	
	while bi < bl:
		b = buf[bi]
		bi += 1
		#print bi
		if b == sign[si]:
			if si == 0:
				pos_bi_save = bi
			si += 1
			if si == sl:
				return bi - si
		else:
			if si > 0:
				bi = pos_bi_save
			si = 0
	return -1


def findDefineInOuptut(line, template):
	p = line.find(template)
	if p <= 0:
		return ''
	p1 = p+len(template)
	p2 = line.find(' ', p1+1)
	if p2 > 0:
		return line[p1:p2].strip()
	return line[p1:].strip()

	
# Extract binary resources from swf-file (using swfdump)
def swfDump(src):
	if not os.path.exists(src):
		print 'File not found:', src
		return
	f = os.popen("swfdump " + src + ' -d')
	extractDump = False
	extractedResName = ''
	extractedResData = []
	extractedResSignature = []
	extractedResType = ''
	for line in f.readlines():
		if extractDump:
			if parseDumpLine(line, extractedResData):
				continue
			else:
				extractDump = False
#				print 'write res', extractedResName
				resFileName = os.path.splitext(os.path.basename(src))[0] + '_' + extractedResName
				resFileName = os.path.join(os.path.dirname(src), resFileName)
				if extractedResType == 'font':
					offset = findSignatureInBuffer(extractedResData, JPG_SIGNATURE)
					if offset >= 0:
						saveToFile(resFileName+'.jpg', extractedResData, offset)
					else:
						saveToFile(resFileName, extractedResData, 0)
				else:
					offset = findSignatureInBuffer(extractedResData, extractedResSignature)
					if offset >= 0:
						saveToFile(resFileName, extractedResData, offset)
					else:
						print 'ERROR: signatre not found', src, '->', extractedResName
		resId = findDefineInOuptut(line, 'DEFINEBITSJPEG2 defines id')
		if len(resId) > 0:
			extractedResName = resId + '.jpg'
			extractedResDump = []
			extractedResSignature = JPG_SIGNATURE
			extractDump = True
			continue
		
		resId = findDefineInOuptut(line, 'DEFINEBITSJPEG3 defines id')
		if len(resId) > 0:
			extractedResName = resId + '.jpg'
			extractedResDump = []
			extractedResSignature = JPG_SIGNATURE
			extractDump = True
			continue

		resId = findDefineInOuptut(line, 'DEFINESOUND defines id')
		if len(resId) > 0:
			extractedResName = resId + '.mp3'
			extractedResSignature = []
			extractedResDump = []	
			extractDump = True
			continue

		resId = findDefineInOuptut(line, 'DEFINEFONT3 defines id')
		if len(resId) > 0:
			extractedResName = resId + '.fnt'			
			extractedResSignature = []
			extractedResDump = []
			extractedResType = 'font'
			extractDump = True
			continue

		resId = findDefineInOuptut(line, 'DEFINEBITSLOSSLESS2 defines id')
		if len(resId) > 0:
			extractedResName = resId + '.img'			
			extractedResSignature = []
			extractedResDump = []
			extractedResType = 'img'
			extractDump = True
			continue

	
		if line.find('DEFINE') > 0 and line.find('defines id') > 0:
			line.find('1')
#			print 'unsupported resource: ', line, 'in', src
		
# parse line of dump and add bytes to array data
# retrn True if line has been read, and Else if dump has ended
def parseDumpLine(line, data):
	p = line.find('-=>')
	if p < 0:
		return False
	p += 4
	p2 = line.find('   ', p)
	if p2 < 0:
		print 'ERROR! corrupted dump line:', line
	dump = line[p:p2].strip().split(' ')
	for v in dump:
		data.append(int(v, 16))
	return True
	

def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		about()
		sys.exit(1)
	swfSrc = os.path.abspath(sys.argv[1])
	print 'SWF file:          ', swfSrc
	outDir = ''
	if len(sys.argv) == 3:
		outDir = sys.argv[2]
	else:
		outDir = os.path.dirname(swfSrc)
	outDir = os.path.abspath(outDir)
	print 'Output directory:  ', outDir

	if not os.path.exists(swfSrc):
		print '  ERROR: source file not found!'
		sys.exit(-1)

	id_shapes = []
	id_movieClips = []
	id_jpegs = []
	id_pngs = []
	id_sounds = []
	id_fonts = []
	id_frames = []
	id_mp3 = []

	beginTime = datetime.now()

	f = os.popen("swfextract " + swfSrc)
	for line in f.readlines():
		if parseSwfExtractOutLine(line, "Shapes: ID(s)", id_shapes):
			continue
		if parseSwfExtractOutLine(line, "Shape: ID(s)", id_shapes):
			continue
		if parseSwfExtractOutLine(line, "MovieClips: ID(s)", id_movieClips):
			continue
		if parseSwfExtractOutLine(line, "MovieClip: ID(s)", id_movieClips):
			continue
		if parseSwfExtractOutLine(line, "JPEGs: ID(s)", id_jpegs):
			continue
		if parseSwfExtractOutLine(line, "JPEG: ID(s)", id_jpegs):
			continue
		if parseSwfExtractOutLine(line, "PNGs: ID(s)", id_pngs):
			continue
		if parseSwfExtractOutLine(line, "PNG: ID(s)", id_pngs):
			continue
		if parseSwfExtractOutLine(line, "Sounds: ID(s)", id_sounds):
			continue
		if parseSwfExtractOutLine(line, "Sound: ID(s)", id_sounds):
			continue
		if parseSwfExtractOutLine(line, "Fonts: ID(s)", id_fonts):
			continue
		if parseSwfExtractOutLine(line, "Font: ID(s)", id_fonts):
			continue
		if parseSwfExtractOutLine(line, "Frames: ID(s)", id_frames):
			continue
		if parseSwfExtractOutLine(line, "Frame: ID(s)", id_frames):
			continue
		if parseSwfExtractOutLine(line, " MP3 Soundstreams", id_mp3): 
			continue
		if parseSwfExtractOutLine(line, " MP3 Soundstream", id_mp3): 
			continue
		s = line.strip()
		if s.find('Objects in file') >= 0:
			continue
		if len(line.strip()) > 0:
			print "WARNING: unknown output: ", line

	print 'Resources:'
	print '   shapes:', len(id_shapes)
	print '   movieclips:', len(id_movieClips)
	print '   JPEGs:', len(id_jpegs)
	print '   PNGs:', len(id_pngs)
	print '   sounds:', len(id_sounds)
	print '   fonts:', len(id_fonts)
	print '   frames:', len(id_frames)
	print '   MP3 streams:', len(id_mp3)

	if not os.path.exists(outDir):
		os.makedirs(outDir)

	print 'Extracting ...'
	extractSwf(id_shapes, swfSrc, outDir, 'shape_', 'swf', '-i')
	extractSwf(id_movieClips, swfSrc, outDir, 'movieclip_', 'swf', '-i')
	extractSwf(id_jpegs, swfSrc, outDir, 'jpeg_', 'swf', '-j')
	extractSwf(id_pngs, swfSrc, outDir, 'png_', 'swf', '-p')
	extractSwf(id_sounds, swfSrc, outDir, 'sound_', 'swf', '-s')
	extractSwf(id_fonts, swfSrc, outDir, 'font_', 'swf', '-F')
	extractSwf(id_frames, swfSrc, outDir, 'frame_', 'swf', '-f')
	extractSwf(id_mp3, swfSrc, outDir, 'sound_', 'mp3', '-m')
	print 'Done. Elapsed time:', (datetime.now() - beginTime)



main()
