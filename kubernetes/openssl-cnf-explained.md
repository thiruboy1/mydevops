# Certificate Authorities & Intermediate CAs
Self-signed CA
keyUsage: cRLSign, digitalSignature, keyCertSign
Should not contain any other KUs or EKUs
V3 Profile:

[ v3_ca ]
basicConstraints        = critical, CA:TRUE
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid:always, issuer:always
keyUsage                = critical, cRLSign, digitalSignature, keyCertSign
subjectAltName          = @alt_ca
Intermediate CA
keyUsage: cRLSign, digitalSignature, keyCertSign
Should not contain any other KUs or EKUs
V3 Profile:

[ v3_ica ]
basicConstraints        = critical, CA:TRUE, pathlen:1
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid:always, issuer:always
keyUsage                = critical, cRLSign, digitalSignature, keyCertSign
subjectAltName          = @alt_ica
Where pathlen: is equal to the number of CAs/ICAs it can sign
Can not sign other CAs/ICAs if pathlen: is set to 0
Non-CA Certificates
VPN Server
keyUsage: nonRepudiation, digitalSignature, keyEncipherment, keyAgreement
V3 Profile:

[ v3_vpn_server ]
basicConstraints        = critical, CA:FALSE
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid:always, issuer:always
keyUsage                = critical, nonRepudiation, digitalSignature, keyEncipherment, keyAgreement 
extendedKeyUsage        = critical, serverAuth
subjectAltName          = @alt_vpn_server
VPN Client
keyUsage: nonRepudiation, digitalSignature, keyEncipherment
V3 Profile:

[ v3_vpn_client ]
basicConstraints        = critical, CA:FALSE
subjectKeyIdentifier    = hash
authorityKeyIdentifier  = keyid:always, issuer:always
keyUsage                = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage        = critical, clientAuth
subjectAltName          = @alt_vpn_client
keyUsage
CA ONLY
keyCertSign

Subject public key is used to verify signatures on certificates
This extension must only be used for CA certificates
cRLSign

Subject public key is to verify signatures on revocation information, such as a CRL
This extension must only be used for CA certificates
digitalSignature

Certificate may be used to apply a digital signature
Digital signatures are often used for entity authentication & data origin authentication with integrity
nonRepudiation

Certificate may be used to sign data as above but the certificate public key may be used to provide non-repudiation services
This prevents the signing entity from falsely denying some action
keyEncipherment

Certificate may be used to encrypt a symmetric key which is then transferred to the target
Target decrypts key, subsequently using it to encrypt & decrypt data between the entities
dataEncipherment

Certificate may be used to encrypt & decrypt actual application data
keyAgreement

Certificate enables use of a key agreement protocol to establish a symmetric key with a target
Symmetric key may then be used to encrypt & decrypt data sent between the entities
encipherOnly

Public key used only for enciphering data while performing key agreement
Req. KU: keyAgreement
decipherOnly

Public key used only for deciphering data while performing key agreement
Req. KU: keyAgreement
RFC 5280 [4.2.1.3]
id-ce-keyUsage OBJECT IDENTIFIER ::=  { id-ce 15 }

Bitstring is hexadecimal

KeyUsage ::= BIT STRING {
    digitalSignature    (0),
    nonRepudiation      (1),
    keyEncipherment     (2),
    dataEncipherment    (3),
    keyAgreement        (4),
    keyCertSign         (5),
    cRLSign             (6),
    encipherOnly        (7),
    decipherOnly        (8)
}
extendedKeyUsage
serverAuth

All VPN servers should be signed with this EKU present
SSL/TLS Web/VPN Server authentication EKU, distinguishing a server which clients can authenticate against
This supersedes nscertype options (ns in nscertype stands for NetScape [browser])
Req. KU: digitalSignature, keyEncipherment or keyAgreement
clientAuth

All VPN clients must be signed with this EKU present
SSL/TLS Web/VPN Client authentication EKU distinguishing a client as a client only
Req. KU: digitalSignature and/or keyAgreement
codeSigning

Code Signing
Req. KU: digitalSignature, nonRepudiation, and/or keyEncipherment or keyAgreement
emailProtection

Email Protection via S/MIME, allows you to send and receive encrypted emails
Req. KU: digitalSignature, keyEncipherment or keyAgreement
timeStamping

Trusted Timestamping
Req. KU: digitalSignature, nonRepudiation
OCSPSigning

OCSP Signing
Req. KU: digitalSignature, nonRepudiation
msCodeInd

Microsoft Individual Code Signing (authenticode)
Req. KU: digitalSignature, keyEncipherment or keyAgreement
msCodeCom

Microsoft Commerical Code Signing (authenticode)
Req. KU: digitalSignature, keyEncipherment or keyAgreement
mcCTLSign

Microsoft Trust List Signing
Req. KU: digitalSignature, nonRepudiation
msEFS

Microsoft Encrypted File System Signing
Req. KU: digitalSignature, keyEncipherment or keyAgreement
