# Linux

# Essential Tools:

## Access Shell Prompt Issue

* how to read man pages
```
man ls
```

## Use Input/Output Redirection

### displaying the file on standard output( > )

1) cat : command(concantate command)

```
cat file1 file2 	# this command will combain both file and dislplay on standard output
cat file1 > /home/txt	
cat file1 file2 >> /home/txt
```

### Redirecting to the input ( < )

```
eg: mysql table_name < backup.sql  #mysql accepts the standard input from backup.sql file 

```

### stadarad error (2>, &>)

```

asdfsd > badcommand.txt # this command will generate error on terminal window if dont want to show on terminal windowo thie use the follosing	
badcommand 2> badcommand.txt # when u execute this, error will not come on the screen insted it will be moved to .txt file
asdfasd 2> /dev/null
/dev/null # is empty space, watever u send it wil be destroyed

./command &> output.txt # this command will redirect standard output and to file not error and discards error
.command 2>& output.txt

```
Redirection standard error to standard output

```
asdfad 2> |grep "command" #this will give error
adadfd 2>& |grep "command" # this will redirect the standard error to grep command through pipe
ls /etc |grep motd # this will redirect standard output to the grep command 
```

## Grep & RegularExpression to Analyze Text

Also refered to as pattern matching, regex or regexp. To keep it simple you can just refer to it as pattern
matching for now.
Pattern can be a character, series of characters, word or sentences.

- grep (global regular expansion print): Linux provides a powerful tool called grep for pattern 
matching. 
The grep tool searches contents of one or more text  files or supplied input for a regular expression. If the expression is matched it prints every line containing


```
Example: 
grep is case sensitive
-v #means inverse
-i # means case insenitive
^ # lines starts with paritiular character

#- grep test /etc/passwd
#- grep 1000 /etc/passwd

Test is the expression that you are searching for in
/etc/passwd file.

#- grep nologin /etc/passwd
Search for nologin

#- grep -v nologin /etc/passwd
To exclude nologin

#- grep -nv nologin /etc/passwd
To exclude nologin and number the lines found


#- grep ^root /etc/passwd
To search for any lines that begin with root.
Caret sign ^ marks the beginning of a line or word.

#- grep ^$ /etc/passwd
To search for all empty lines in /etc/passwd


#- grep -i root /etc/passwd
To perform case-insensitive search for root in a file.
i = case insensitive 

grep [lL]inuxacademy # this will check for either l or L

grep 'l...x' file # this command will check for l and x in bw any 3 character can be exists
grep 'nologin' /etc/passwd
#- cat  /etc/passwd  | egrep 'test|root'
Searches for patterns test and root in /etc/passwd.

| (pipe) can send output of one command as input to 
the next. More on pipe in the next section.
```


## Access Remote Using SSH

### What is ssh
https://www.tecmint.com/protect-ssh-logins-with-ssh-motd-banner-messages/

Introduction to SSH Secure Shell: 
Secure Shell SSH provides a secure mechanism for data transmission between source and destination systems over IP networks. 
It replaces older remote login programs that transmitted user password in clear text(Telnet) and unencrypted data.
SSH uses encryption for secure communication and digital signatures for user authentication.
It also ensures integrity of the data being transfered.
SSH includes a set of utilities and provides remote  users the ability to login, transfer files and securelyexecute commands. 
SSH utilities have widely replaced other unsecure login and file transfer programs.
SSH operates over port 22, unless you configure it otherwise. 
```
Example: 
#- ssh servername (test)
#- man ssh
```
### When to use SSH

When is SSH used?


Most servers are located in data centers or equipment  racks far away from the system admins and users.
Same is true for routers, switches and other network devices.
In most cases it's not practical to physically visit the console of each server that you manage, so instead we install SSH clients susch as PuTTY or TeraTerm onWindows computers or OpenSSH on Macs and nix computers.
We can then use such software to log in across the network to the remote servers and other network devices.
That is how system administrators manage servers from  the command line as though they were actually sitting at the physical console.

### How to configure SSH

How to configure SSH?
```
Once SSH is installed, configuration file is located in /etc/ssh/sshd_config.

Within this file you can modify things such as:

-The listening IP adress
-TCP Port number (Default is 22)
-Logging options
-Authentication options

```
Before making any changes to this file make sure to  make a backup of the original file for safety.

Example:
```
#:- cat /etc/ssh/sshd_config
```

### Securing SSH



From security standpoint, there are two easy things to do to make SSH secure:
```
1- Change the default port:

The default port is 22, but its easy to change it to something else within the dynamic port range of 49,153 to 65,535. 
A hacker running a system wide port scan can still  discover it but it is better than having port 22 as a default which almost everyone knows.
Usually hackers are looking for easy targets and they move on to an easier target if it takes too long.


2- Disable root login:

On most internet connected servers, usually logs will indicate tons of attempts using username root by the
bad guys.
Everyone knows Linux admin username is root so they will try to penetrate the system with that username first.

Example:
- Make a backup of sshd_config
- vi /etc/ssh/sshd_config
- Change port 22 to 5000
- Change PermitRootLogin from yes to no

Note: Now you will have to login with a regular user instead of root via SSH.
 
```

### Transferring Files with SCP:

SCP stand for secure copy and is a part of SSH suite. It allows you to transfer a file securely from one server to another.

Example: 
```
#: scp file1 root@servername:/
To copy file1 from current location to another server under the directory /.
Note: You don't need to specify the user name if logging in with the same username.
```
Connecting through sftp: 

SFTP is installed as part of the SSH suite.  It allows secure transfer of files as well as secure authentication. Like SSH, SFTP also operates on the same port 22.
```
Example:

#: sftp servername
```

### Configure Private-Public Key-Based Authentication:

In this example you will generate private/public key combination for a user on one server and use it to allow this user to access another server using the ssh command.
```
1- log onto centos (server name)
2- ssh-keygen
3- cat /home/user1/.ssh/id_rsa
4- ssh-copy-id -i id_rsa.pub test(server name)
5- ssh test as user2
```

### OpenSSH
Openssh is a free and open source implementation of SSH. Once applied on the system - telnet, rlogin, rsh, rexec, and ftp services can be disabled to enhance security.

The ssh command has replaced telnet, rlogin, rsh, rexec and rcp,ftp commands have been replaced by scp, sftp respectively. 



Example: 
```
- To transfer files securely from source to destination:

#- scp  /file1  servername:/file1

#- ssh user@servername

#- man ssh

 ssh (SSH client) is a program for logging into a  remote machine and for executing commands on a remote  machine.  It is intended to provide secure encrypted  communications between two untrusted hosts over an  insecure network.  X11 connections, arbitrary TCP  ports and UNIX-domain sockets can also be forwarded  over the secure channel.
```

### OpenSSH 
Openssh currently supports 2 versions: v1 and v2. Both  are available in RHEL/Centos 7. Newer version should used as it has enhanced features  and configuration options.

Configuration file is located in /etc/ssh/sshd_config.
```
#- cat /etc/ssh/sshd_config
Check for installed ssh packages:
#- rpm -qa | grep ssh.


- Both versions support various algorithms for data  encryption and user authentication (digital signatures).

OpenSSH v1:  Supports the RSA Algorithm only.
OpenSSH v2:  Supports RSA, DSA and ECDSA.
RSA: Rivest-Shamir-Adleman, who first published this Algorith.
RSA is most commonly used becuase it supports both encryption and digital signatures.

DSA: Digital Signature Algorithm

ECDSA: Elliptic Curve Digital Signature Algorithm.
```

### Encription

Encryption is a way of transforming information into a  scrambled form to conceal the real informtion from  unauthorized access. 
Encryption is done at the client end and the reverse process is de-encryption, which is on the server end.
OpenSSH uses many encryption techniques during an end  to end communication session.
These techniques include symmetric and asymmetric encryption. 


* Symmetric Encryption: 

This type of encryption uses a single secret key or a pair of keys to protect authentication traffic as wellas the entire communication session. 
This key is generated as a result of a negotiation  process between the client and server.


* Asymmetric Encryption:
This encryption uses a private/public key combination for encryption. These keys are randomly generated alphanumeric characters attached to messages during acommunication session. 
The client transfers the information using a public key and the server decrypts it using the paired private key.
The private key must be kept secure since it is private to that one system only. The public key is distributed to clients. 
This method is used for channel encryption as well as  for user authentication. 



### Authentication 
Once an encrypted channel is established between the  client and server, additional negotiations take place between the two to authenticate the user trying to gain acces to the server. 


Open SSH offers several methods for this purpose, listed  below in the order in which they are attempted duringthe authentication process:

- GSSAPI - based authentication
- Host based authentication
- Private/Public key based authentication
- Challenge response authentication
- Password based authentication


GSSAPI - based authentication: 
It provides a standard interface that allows security mechanism such as Kerberos to be plugged in. OpenSSH uses this interface and kerberos for authentication.
With this method, an exchange of tokens takes place between the client and server to validate user identity.
This method is only supported in OpenSSH version 2.


* Host based authentication:  Allows a single user, a group of users or all users on the client to be authenticated on the server. A user may be configured to login with a matching user
name on the server or as a differnt user that exists on the server.
Each user that requires an automatic entry on the server a .shosts file is set up in the user's home directory.
Group of users or all users setup is done in the  /etc/ssh/shosts.equiv file.

* Private/Public key based authentication: This method uses a private/public key combination for user authentication. The user on the client has a publickey and the server stores the corresponding private key.When user tries to login, the server prompts the user to enter the key and lets the user login if the key is validated.
* Challenge response authentication: This method is based on response to one or more  challenge questions that the user has to answer  correctly in order to gain login access to the server.
* Password based authentication: Server prompts the user to enter their password. It checks the password against the stored entry in the /etc/shadow file and allows the user to login if the password is confirmed.


## Login & Switch  Users in Multiuser Targets

```
systemctl get-default # this command will get the default targets
su #this command allows use to login to diffrent user , switch user, but here if u notice user profile will not be loaded
su -l #is login shell, this will use all custom profiles of user
```
- Interactive: (bashrc is loded)As the term implies: Interactive means that the commands are run with user-interaction from keyboard. E.g. the shell can prompt the user to enter input.
- Non-interactive: the shell is probably run from an automated process so it can't assume if can request input or that someone will see the output. E.g Maybe it is best to write output to a log-file.
- Login: (bash_profile is loded)Means that the shell is run as part of the login of the user to the system. Typically used to do any configuration that a user needs/wants to establish his work-environment.
- Non-login: Any other shell run by the user after logging on, or which is run by any automated process which is not coupled to a logged in user.
- interactive shell: when ever u switch user it will be using interactive shell were user bash_profiles will not be loaded


Switching Users: 

* Logging in to the system directly as root is not  recommended. The recommended practice is to log on with  normal user account and then switch into the root  account if necessary.

* In addition to becoming root, we can also switch into  another user account. Unless you are root, you need to know the password for the target user account you are switching to.

* The su command can used to switch into another user account.
```
Example: 

- To switch from a user to root without executing  startup scripts for the target user:
#- su
Password (root pw)
- To switch into a different user account from user1 to user2, specify the name of the target user with the
command: 
#- su - user2
Password (user2 password)
- You can also issue a command as a different user  without switching into that user: 

#- su -c 'firewall-cmd --list-services'
Password (root password)

-c option is available with su.
- firewall-cmd --list-services requires superuser
privileges.
- users can use su to execute privileged commands. 
- User root can switch into any account without beingprompted for that user's password.
#- su user1

```

### The sudo utility: 

Linux gives normal users the ability to run privileged commands. There is a utility called sudo that can be  used for this purpose.


- For example, a regular user can run useradd command  with sudo if they have been granted access: 
#- sudo useradd
password


- Rights provided to sudo users can be used to allow a user or a group to run scripts and applicationsowned by a different user.


- Rights an be provided by editing a file /etc/sudoers.
- File can be edited by using visudo command.

- To give ALL privileges to administrative commands on  the system to both a user called test and a group 
called wheel, add the below line to /etc/sudoers file: 

```
test    ALL=(ALL)      ALL
%wheel  ALL=(ALL)      ALL

```
- To give access to users and groups so they can run privileged commands without getting prompted for a password, below lines can be added to sudoers file.
```
test    ALL=(ALL)    NOPASSWD: ALL
%wheel  ALL=(ALL)    NOPASSWD: ALL

```
- Rights can also be granted to users and groups in  a restricted way:
```
user	All=/usr/sbin/userdel,/usr/sbin/adduser
%wheel	All=/usr/sbin/userdel,/usr/sbin/adduser
```

## Archive  Compress 

Compression Tools:

- Compression tools are used to compress one or more files or an archive to save space.

###  gzip

This command creates a compressed file of each of the files specified and adds .gz extension to the files.

- Example: 
```
#- gzip filename
#- ls or ll (check files after compression)

- To uncompress use:
#- gunzip filename
or
#- gzip -d filename
# ls or ll (check files after decompression) 

---

You can also use bzip2 and bunzip2

#- bzip2 filename
#- bunzip2 filename or bzip2 -d filename

---
```
###  Archiving tools: 

- tar (tape archive)command creates, appends, updates lists and extracts files to and from a single file called tar file (aka tarball)

Example: 
```
#- tar 

options:
-c (Creates a tarball)
-v (Verbose mode)
-f (Specifies a tarball name)
-t (Lists contents of a tarball)
-x (Extracts from a tarball)
-z (Compresses a tarball with gzip command)

#- tar cvf example.tar  example  Creates tarball example.tar of the file example
#- tar tvf example.tar To list contents of tarball example.tar
#- tar xvf example.tar To extract file example.tar
#- tar cvzf example.tar.gz example Creates a tarball and compresses it with gzip
#- tar xvzf example.tar.gzgzip

````

### star 
- we can use find command in star and star will not oviried the files during extraction
- it gives extraprotection on file (by not overiding)
- u can extract only specfic file
```
star -c -f=filename.tar files # creates tar file
star -t -f=filename.tar	# displays content of tar
```




## Create and Edit Text Files
- Files can be create in multiple ways. However, directories can only be created with one command.

- Creating File with touch command: 
```
Examples: 
#- touch file1
#- ls
#- touch file2 file3 file4
#- ls
Note : If the file already exists, it will update the
timestamp on it to the current date and time.

```
- Creating files with vi editor: 
Examples: 
```
#- vi filename
- add text
- save and exit 

```
- Creating directories using mkdir command:
Examples: 
```
#- mkdir dir1
To create a directory called dir1

#- mkdir a b c 
To create 3 directories a b c.

#- mkdir -p 1/2/3
To create hierarchy of sub-directories.
```
### File Type 
Linux (Currently using RHEL 7.4 distro) supports several different types of files.


Some of the common file types are listed below: 
- Regular files
- Directory files
- Executable files
- Symbolic link files
- Device files


- Regular files: Regular files may contain text or binary data. These files could be command in the binary form or shellscripts.
Examples:
```
#- ls /bin
#- file .bash_profile
```

- Directory files:  Directories are logical containers that are used to  hold files and sub-directories.
Examples:
```
#- ll /  
Letter d at the begining identifies the file as a directory.
#- file / 
Identifies / as a directory
```

- Executable Files: Any file that can be run is an executable, they could be shell scripts or binary commands.
Examples: 
```
#- ll /usr/bin (x means it is executable)
#- file /usr/bin/whoami (executable command)
```

- Symbolic link files(aka symlink or softlink):  These can be considered as a shortcut to another file or directory. Begins with letter l and shows an arrow.

Examples: 
```
#- ll /usr/sbin/vigr
l = soft link
-> = point to original file
#- file /usr/sbin/vigr
```
- Device Files:  Each piece of hardware in the system has an associated file called device file. 
```
Two types of device files are: 
- character (or raw) device file,(keybord)
- block device file

Examples: 
#- ll /dev/sda 
#- ll /dev/tty
First character b represents block device file
First character c represents character device file.

#- file /dev/sda
#- file /dev/tty
```

### Listing Files

- Use ll command to list files and directories.
```
#- ll 
drwxr-xr-x. 3 root root 15 May  9 20:50 1
```
* Break down by Columns: 

- Column 1: drwxr-xr-x. #First charcter indicates a directory, next 9 characters indicate permissions.
- Column 2: 3 #Displays the number of links.
- Column 3: root #Shows the owner name.
- Column 4: root #Displays the owning group name.
- Column 5: 15 #Identifies the file size in bytes. For directories this number reflects the number of blocks being usedby directory to hold info about its contents.
- Column 6,7 and 8:  May  9 20:50 1 #Displays month, day of month and last modified time.
- Column 9: 1 #Name of the file or directory.


### VI & VIM
vim #highlits the syntax

There r 2 modes
- insert mode(press i)
- command mode(escap key)

wq #save and quit
dd #cut the line
shift+g #top of the file
cc #will remove the line and goes to insert mode
? #to search text
/ #to search text
:%s/word/hello/g #to replace text in command mode

## Create Delete copy move files and Directory 
yum install tree #to c directory structure


cp file1 file2 #- Copy file1 and name the copied file file2

```
- Delete a file
#- rm file2
#- rm -f filename (without asking for confirmation)
```
mv file1 to file3 #Rename or move a file
mkdir dir1 #Create a Directory called dir1
rmdir dir1- Remove a directory

- Remove a directory with files in it.
```
#- rm -rf dir1
-r = recursively
-f = forcefully
```

- List history of your commands
```
#- history

- Re run a command from history by number
#- !# (# represents the command number)
```


## Hard Links & Soft Links


- Before looking at soft and hard links, let's look at  some basics that you must understand:
- Let's look at the result of below command: 
```
#- ll /usr/sbin/vigr 

lrwxrwxrwx. 1 root root 4 Dec 20 06:10 /usr/sbin/vigr -> vipw
```
- Each file in a system has many attributes assigned to  it at the time of its creation known as metadata. These include file's type, size, permissions, owners nameowners group name, ACL, links and other related info.

This metadata info has to be stores somewhere. This metadata info takes only 128-bytes of space and this tiny storage space is knows as inode (index node) Inode assigns a numeric identifier to each file which is used by the kernel.
To find out inode number of a file use below command:
```
#- ll -i /usr/sbin/vigr 

99699 lrwxrwxrwx. 1 root root 4 Dec 20 06:10 
/usr/sbin/vigr -> vipw

99699 = inode number

```

### Soft and hard links

### Soft links (aka symlink or symbolic link):  

Soft links(shortcuts) are similar to a short cut in windows, they point to another file.if u edit the symlink the ur actuly editing source file
- u can any number of symlink for the same file 
- if u delete or remove the target file then symlink will be broken
- and if u try to create the file then new file will be created
- symlink can be used accors filesystems

Example: 
- Create a soft link called file2 to an existing file called file1: 
```
#- ln -s file1 file2
#- ll file2
lrwxrwxrwx. 1 root root 5 May 10 15:34 file2 -> file1

l = soft link
-> = points to the linked file
```

- Show inodes of both files:
```
#- ll -i file*
```
Inodes assigned to both files are different.

Note: If the original file is deleted symlink becomes  useless as it is a shortcut to a file that does not exist.

- Hard link: 

Hard link associates one or more files with a single inode number unlike a softlink. This also implies that any changes made to original  file will also be applied to the hard linked file.
Example: 
- hard link can be used to link file systems
- Create a hard link called file2 to an existing  file called file1. 
```
#- ln file1 file2
#- ll -i file*

200622 -rw-r--r--. 2 root root 0 May 10 15:34 file1
200622 -rw-r--r--. 2 root root 0 May 10 15:34 file2

As you can see both files have the same inode number. 200622 is the inode number 2 represents number of hard links

Note: If one file is deleted the other file will  exist unlike a symlink.
```

## List Set and Change Standard UGO/RWX Permission

### Understanding permissions

Let's look at permissions of file1 and file2:
```
#- ll file1 and ll file2
-rwx-w---x. 1 root root 0 May 10 15:34 file1
-rwxrwxrwx. 1 root root 0 May 10 16:18 file2

r = read
w = write
x = execute/to navigate insde directory
X = 

u = user owner
g = group owner
o = others (or public)
```
###  Modifying permissions

Let's look at permissions of file1:
```
#- ll file1 and ll file2
-rwx-w---x. 1 root root 0 May 10 15:34 file1
-rwxrwxrwx. 1 root root 0 May 10 16:18 file2
	

r = read
w = write
x = execute

u = user owner
g = group owner
o = others (or public)

r = read     = 4
w = write    = 2
x = execute  = 1
rwx   =	       7 

rwx-w---x     and  rwxrwxrwx
7   2   1	   7   7   7
```
- Change rights of a file and grant full rights to user, group and others through octal notations.
```
#- ll
#- chmod 777 file
#- ll
```
- Change rights of a file - remove read, write and execute rights for group and others via symbolic notation.

```
chmod go-rw file 
chmod ug+X # allows user to access directory but not scripts , none of scripts will excecute permission
chmod ug+rwx -R docs # apply permission recursively on all directorys
```
To re-add read and write rights back to group &  others:
```
#- chmod go+rw
$- ll file
```
- Assign read rights to all users
```
#- chmod a=rwx
a = all
```
### default permissions
Linux assigns default permissions to a file or a directory at the time of creation. 

Default permissions are calculated based on the  umask (user mask)permission value subtracted from a  preset value called "initial" permissions.
Default permission = umask - initial
Example:
```
Create a file as a regular user 
#- touch file
#- ll
-rw-rw--r--. 1 root root 0 May 10 17:04 file
6   6   4

readwrite-readwrite--read-- (default permissions)

```
### UMASK 
when ever we create directory/file it will set the default-permission, this default permission will come from umask


* umask can be changed using sudo vi /etc/profile
* u can change umask value in bashrc file, (for root umask will be 666-002 and other users 666-022)
* root user will have id of 199
To find umsak value:
```
#- umask
002
umask can be changed using sudo vi /etc/profile
For regular users: 
- Initial permissions = 666 for files 
- Initial permissions = 777 for directories 
Files: 
- Initial permissions - umask = Default permission  
  666 - 002 = 664

-rw-rw--r--. 1 root root 0 May 10 17:04 file
6   6   4
```
Directories: 
```
- Initial permissions - umask = Default permission
  777 - 002 = 775
Example: 
#- mkdir 2 (as regular user)
#- ll 2
drwxrwxr-x. 2 1 1 6 May 10 17:20 2
7  7   5
``` 



### Setuid,Setgid & stickbit
Linux offers 3 types of special permission bits that maybe set on executable files or directories to  respond differently for certain operations.

These special permission bits are:
```
- setuid (set user identifier) bit
- setgid (set group identifier) bit
- sticky bit
```

- The setuid and setgid:
- These 2 bits can provide non-owners and non-group owners the ability to run executables with same accessas the owner and group owner.

### Setuid bit: this setuid bit on executable files: Setuid bit flag can provide regular users the ability to run the same access as the owner of the executable  file.

It is represented by an s in the owner's permission class. 
Example: 
```
#- ll /usr/bin/su
-rwsr-xr-x. 1 root root 32096 Dec  1 18:28 /usr/bin/su
s = setuid bit
- Login with a regular user and run su command.
- Lets remove the setuid flag 
#- chmod u-s /usr/bin/su
#- ll /usr/bin/su
-rwxr-xr-x. 1 root root 32096 Dec  1 18:28 /usr/bin/su
```
Setuid bit has been removed, let try to run su again  as a regular user.
su: Authentication failure

- To re-add setuid bit:
```
#- chmod u+s /usr/bin/su
#- ll /usr/bin/su
-rwsr-xr-x. 1 root root 32096 Dec  1 18:28 /usr/bin/sure-added setuid bit represented by s.
```
- You can also use numbers to apply setuid bit.
```
chmod u+s /usr/bin/su
or 
chmod 4755 /usr/bin/su
```
4 adds the the setuid bit.

find / -perm -4000 To search for all files with setuid bit permissions:


### Setgid bit on executable files:

- Setgid bit is set on executable files at the group  level. Setgid bit flag can provide regular users the  ability to run the same access as the group members of 
the executable file.
It is represented by an s in the group's permission class. 

Example: 
```
#- ll /usr/bin/wall
-r-xr-sr-x. 1 root tty 15344 Jun  9  2014 /usr/bin/wall
s is the stickybit flag in group permissions

chmod g-s /usr/bin/wall #To remove setgid bit: 
chmod g+s /usr/bin/wall #To add setgid bit: 
 or 
chmod 2555 /usr/bin/wall


find / -perm -2000 #To search for all files with setgid bit permissions:
```
-------------

### Stickybit: 

Sticky bit is set on public writeable directories to 
prevent moving or deletion by regular users.

Example: 
```
ll -d /tmp
drwxrwxrwt. 7 root root 93 May 11 04:00 /tmp/
t = stickybit in other's permissions
- The stickybit can be set by following command:

- Create a directory
#- mkdir dir1

-Add stickybit with rwx permissions to all
#- chmod o+t /tmp
#- chmod 777 /tmp
or
#- chmod 1777
#- ll dir1

chmod o-t dir1 # To remove stickybit or
chmod 777 dir1
chmod 7777 # will set all permission
1 sets the sticky bit.

find / -type d -perm -1000 # To search for all files with stickybit permissions:
```

## Locate Read and use System Doc with man info and /usr/share/doc

```
man 5 passwd #this will open manual page 5 for passwd
apropos passwd # this command will search for man page index,before running this command cache the man page by running following command 
mandb #caching man page 
which # comand
apropos

```

## Finding files with locate and find
- Typical running Linux system has hundreds and  thousands of files. You may need to search for a files by a particular user or search file by their size.

1) Locate: 
2) Find

1) Locate: is command to find the files in the system, locate is cached and its updated by cron daily
however we can manualy update the cache  

updatedb # this command will update he cache of locate command

locate httpd 


2) Find:


```
find / -name fi* -print Using the find command 
find = command
/ = Path or location we want to search
name = search option (search by name)
print = action (print is default so no need to type it)
delete = action

```
Example: 

- Find all files named "file1": under / directory and delete them all: 
```
#- find / -name files
#- find / -name files -delete
#- #- find / -name files
find / -perm -4000
find /etc/ -name motd
find /etc/ -user root #finds all files related to the root user
find / -mtime -3 #find all files that was modified last 3 days
find / -mtime +3 #find all files that was not modified last 3 days
find / -user thiru

```
### stat /etc/profile #this command will provides info about last modified date and time
- Find files smaller than 1 MB in root's home directory
-  find / -size -1M
- Find files smaller than 1 MB in current directory.
```
find . -size -1M
"." represents current director
- To find files in /usr, larger than 40MB
#- find /usr -size +40M
- Find files that were modified 4 days ago:
#- find /var -mtime 4
#- man find 
To learn more about find command.
```
 


# Operate Running System:

## Boot, Reboot and shutdown a system

- new redhat use systemd which handels the initilization of filesystem, it handles reboot shutdown and all activitys

Reboot: 
```
systemctl reboot
shutdown -r now # reboot immidetly
shutdown -r +5 #reboot wait 5 min before reboot, during it sends wall mesasge to all logined users
if u want cancel the reboot before 5min(defined time) then u can use follwing command
shutdown -c # this will cancle the shutdown  
```
what happens wen u call for reboot?
```
brings the system down in a secure way. 
All logged-in users are notified that the system is going down, and login(1) is blocked. 
It is possible to shut the system down immediately or after a specified delay. 
All processes are first notified that the system is going down by the signal SIGTERM. 
So basically reboot calls the "shutdown".

```

Power off : 
```
shutdown -h 
shutdown -h +5
```

## Boot System into diffrent targerts

### Boot Porcess?
```
1. BIOS
BIOS stands for Basic Input/Output System
Performs some system integrity checks
Searches, loads, and executes the boot loader program.
It looks for boot loader in floppy, cd-rom, or hard drive. You can press a key (typically F12 of F2, but it depends on your system) during the BIOS startup to change the boot sequence.
Once the boot loader program is detected and loaded into the memory, BIOS gives the control to it.
So, in simple terms BIOS loads and executes the MBR boot loader.

2. MBR
MBR stands for Master Boot Record.
It is located in the 1st sector of the bootable disk. Typically /dev/hda, or /dev/sda
MBR is less than 512 bytes in size. This has three components 1) primary boot loader info in 1st 446 bytes 2) partition table info in next 64 bytes 3) mbr validation check in last 2 bytes.
It contains information about GRUB (or LILO in old systems).
So, in simple terms MBR loads and executes the GRUB boot loader.
3. GRUB
GRUB stands for Grand Unified Bootloader.
If you have multiple kernel images installed on your system, you can choose which one to be executed.
GRUB displays a splash screen, waits for few seconds, if you don’t enter anything, it loads the default kernel image as specified in the grub configuration file.
GRUB has the knowledge of the filesystem (the older Linux loader LILO didn’t understand filesystem).
Grub configuration file is /boot/grub/grub.conf (/etc/grub.conf is a link to this). The following is sample grub.conf of CentOS.
#boot=/dev/sda
default=0
timeout=5
splashimage=(hd0,0)/boot/grub/splash.xpm.gz
hiddenmenu
title CentOS (2.6.18-194.el5PAE)
          root (hd0,0)
          kernel /boot/vmlinuz-2.6.18-194.el5PAE ro root=LABEL=/
          initrd /boot/initrd-2.6.18-194.el5PAE.img
As you notice from the above info, it contains kernel and initrd image.
So, in simple terms GRUB just loads and executes Kernel and initrd images.
4. Kernel
Mounts the root file system as specified in the “root=” in grub.conf
Kernel executes the /sbin/init program
Since init was the 1st program to be executed by Linux Kernel, it has the process id (PID) of 1. Do a ‘ps -ef | grep init’ and check the pid.
initrd stands for Initial RAM Disk.
initrd is used by kernel as temporary root file system until kernel is booted and the real root file system is mounted. It also contains necessary drivers 
compiled inside, which helps it to access the hard drive partitions, and other hardware.
5. Init
Looks at the /etc/inittab file to decide the Linux run level.
Following are the available run levels
0 – halt
1 – Single user mode
2 – Multiuser, without NFS
3 – Full multiuser mode
4 – unused
5 – X11
6 – reboot
Init identifies the default initlevel from /etc/inittab and uses that to load all appropriate program.
Execute ‘grep initdefault /etc/inittab’ on your system to identify the default run level
If you want to get into trouble, you can set the default run level to 0 or 6. Since you know what 0 and 6 means, probably you might not do that.
Typically you would set the default run level to either 3 or 5.
6. Runlevel programs
When the Linux system is booting up, you might see various services getting started. For example, it might say “starting sendmail …. OK”. Those are the runlevel programs, executed from the run level directory as defined by your run level.
Depending on your default init level setting, the system will execute the programs from one of the following directories.
Run level 0 – /etc/rc.d/rc0.d/
Run level 1 – /etc/rc.d/rc1.d/
Run level 2 – /etc/rc.d/rc2.d/
Run level 3 – /etc/rc.d/rc3.d/
Run level 4 – /etc/rc.d/rc4.d/
Run level 5 – /etc/rc.d/rc5.d/
Run level 6 – /etc/rc.d/rc6.d/
Please note that there are also symbolic links available for these directory under /etc directly. So, /etc/rc0.d is linked to /etc/rc.d/rc0.d.
Under the /etc/rc.d/rc*.d/ directories, you would see programs that start with S and K.
Programs starts with S are used during startup. S for startup.
Programs starts with K are used during shutdown. K for kill.
There are numbers right next to S and K in the program names. Those are the sequence number in which the programs should be started or killed.
For example, S12syslog is to start the syslog deamon, which has the sequence number of 12. S80sendmail is to start the sendmail daemon, which has the sequence number of 80. So, syslog program will be started before sendmail.
```


### Targets: 
Systemd has replaced sysVinit as the default service  manager in RHEL 7. Some of the sysVinit commands have been symlinked to their RHEL 7 counterparts, however  this will eventually be deprecated in favor of the standard systemd commands in the future.
Systemd uses Targets instead of the runlevels.
* to check targtes installed in my system
```
systemctl get-default #this will show the current target
systemctl list-units --type=targets 
systemtl -t help #to list all type of unit config file in system we mostly use service & target 
```
insted of writing startup scritp we wirte service, this are the services located in following directory 
```
cd /usr/lib/systemd/system

sshd.service file
[Unit]
Description=OpenSSH server daemon
Documentation=man:sshd(8) man:sshd_config(5)
After=network.target sshd-keygen.service		#should start only after network target started
Wants=sshd-keygen.service

[Service]
Type=notify
EnvironmentFile=/etc/sysconfig/sshd
ExecStart=/usr/sbin/sshd -D $OPTIONS  			# before start execute this
ExecReload=/bin/kill -HUP $MAINPID			# when we issue ssh reload command execute this
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target				# when system moves to multi user target then unit config file will be called
```
systemctl list-dependencies multi-user.target # this will displa the dependence of targets

 
- Each Runlevel Target file is a symbolic link to the system-start Target equivalents. For example:
```
# cd /usr/lib/systemd/system
# ls -l runlevel*
```
Comapring runlevel with Target: 
```
Runlevel 0 – shut down the system
Runlevel 1 – single mode
Runlevel 2 – multiuser mode without networking
Runlevel 3 – multiuser with text login screen
Runlevel 4- customized runlevel (not in use)
Runlevel 5 – runlevel 3 with graphical login
Runlevel 6 – Reboots the system

````
Targets: 
```
0- runlevel 0.target, poweroff.target 
System halt/shutdown

1- runlevel1.target, rescue.target
Single-user mode (rescue mode)

2- runlevel2.target
User-defined/Site-specific runlevels. By default, 
identical to 3.

3- runlevel3.target, multi-user.target
Multi-user, non-graphical mode, command line

4-  runlevel4.target
User-defined/Site-specific runlevels. By default, 
identical to 3.

5- runlevel5.target, graphical.target
Multi-user, graphical mode

6- runlevel6.target, reboot.target
Reboot

- emergency- emergency.target Emergency mode. Root fs is mounted read only, no other fs are mounted and no networking either.


```


- Managing Targets

Viewing and setting Default boot Target:
```
- To check current default boot target
# systemctl get-default

multi-user.target

- To change default boot target: when u run this default.target symlink will point to the multi-user.target
# systemctl set-default multi-user.target

-----

Switching into specific targets: to move from one target to another target we can use systemctl isolate <target> command

- Switch to graphical target (Legacy runlevel 5)
# systemctl isolate graphical.target

- Switch to multi-user Target (Legacy runlevel 3)
# systemctl isolate multi-user.target

- Shutdown system to halt state:
# systemctl halt

- Shutdown and power off
# systemctl poweroff

- Reboot
# systemctl reboot

- To switch to Legacy runlevel 3 Target:
# systemctl isolate runlevel3.target
```
### going to rescue target/emergency target

- reboot
- go to boot menu and press up/down arrow key so that it takes away timer count
- press e to edit the item
- and search for vmlinx16 kernel edit the kernel command line , eg: linux16 , and at end of the line add systemd.unit=rescue.target
- ctrl+x to contionue the boot process 


## Intrupt Boot Process to Gain Access to a system


### reseting root password

initial when system boots up it hands the control to grub, when we select kernel, kernel needs to be loaded somewhere, so grub allow us 
to load local kernel inside memory that kernel has systemd and root device that gona map, it mounts feature root device 
as sysroot and initramfs and hands over control to initrms, so now we have to break into that process and get into
initramfs debug shell and change password 

* step 1) boot the system in rescuemode/recovery mode (reboot, go to boot menu and press up/down arrow key so that it takes away timer count)
* step 2) search for vmlinx16 kernel edit the kernel command line , eg: linux16 , and at end of the line add "rd.break" this will take us to initramfs debug shell
- go to shell 
* notes: contents are mounted as sysroot, once initramfs is completed booting then its gona take contens from sysroot and mount it as root directory
so we should make sure that mount that as root device using chrot
now first we have to remount the sysroot directory as read wirte options
- now the system will be read mode to enable it in write mode
* step 3) mount -o rw,remount/          #remount sysroot for read write
now i want to mount sysroot directory as my local root directory the reson i want to do is i want to run passwd command, i want to able to edit /etc/passwd directory

* step 4) chroot /sysroot
* step 5) passwd
* step 6) touch /.autorelable  #since selinux is enable, we have to relable all our file just we have to make sure that file exists
if this file exits the systme will instruct to relable if not passwd change will not be successfull
* step 6) shutdown -r
 

## Adjust Process Priority and Kill Porcess 

### Understanding Processes: 

- A process is a unit for provisioning system resources. It is any program, application or command that runs on the system.
- A process is created in memory in its own address space when a command, program or application is initiated.
- Processes are organized in a hierarchial fashion.
- Each process has a parent process a.k.a. a calling process that spawns it.
- A single parent process may have one or more child processes and processes many of its attributes to them when they are created.
- Each process is assigned a unique identification number knows as PID (Process identifier), which is used by the kernel to manage and control the process through its lifecycle.
- Once the process is completed or terminated, this event is reported back to its parent process and all there sources assigned to it are then freed and the PID is removed.
- Several processes are started at system boot, many of which sit in the memory and wait for an event to trigger a request to use their services.
- These background system processes are called daemons and are critical for the system to operate.



ps: is used to find the process running on our system
- An operational system can have hundreds or thousands of running processes depending on its purpose.
- We can view and monitor these processes using various native tools such as ps (process status) and top.



 pgrep
```
pgrep
pgrep -u thiru -l #display all process running by the user thiru
pgrep -u thiru -l vi #display all process running by the user thiru and using vi
pgrep -v root  #-v is invert, all process not owned by root
```
pkill
```
pkill httpd
pkill -t pts/1  #this will kill all process run by the terminal ("who" to know the terminal id)
pkill -u thiru sshd
pkill -9   # (SIGKILL)this will kill the process immedittly
```
kill -l
```
SIGKILL #kills process immeditly
SIGINT #Keyboard Intrupt
SIGHUP #use to report termination,similar closing terminal which informs to all process
SIGQUIT #requesting process to quit
SITTERM #terminate the process
SITSTP # stop the process
SIGCONT #u can stop process and u and continue using this process
```

### create process and send to bacground, and kill to stop prcess


- jobs # to check bacground process
```
(while true; do echo -n "My Program" >> ~/output.file; sleep 1; done) $ #this will create a job in bacground
jobs
kill -SIGSTOP %1 # stops the job number 1
kill -SIGCONT %1 #runs the stopped job number 1
kill -SIGTERM %1 #Terminates the job number 1
```





- The ps command: 
Shows basic process information in four cloumns.
The ps command without any options or arguments lists processes specific to the terminal where this command is run.
```
#: ps

 PID TTY          TIME CMD
12034 pts/0    00:00:00 bash
12749 pts/0    00:00:00 ps
```
Above output shows basic information in four columns.

PID = process ID number.
TTY = Terminal the process belongs to.
TIME = Cumulative time CPU has given to this process.
CMD = Name of command or program being executed. 

Commonly used options with ps command include:
-a = all
-e = every
-f = full-format
-F = Extra full format
-l = long format
-u = user specfic


Example: 

```
#: ps -eaf

UID = User ID or process owner's name.
PID = Process ID number.
PPID = Process ID of the parent process.
C    = Processor utiliztion for the process.
STIME = Process start date or time.
TTY = Terminal the process belongs to.
TIME = Aggregated execution time for the process.
CMD = Name of command or program being executed.
```
Information of each running process is maintained and kept in the /proc file system.
- View Processes by User and group ownership:- 
- A process can be listed by its ownership or owning group. We can use the ps command for this purpose.
For example: 
```
- To list all processes owned by root, specify the -U option with the command and username: 
#- ps -U root
[root@centos ~]# ps -U root
  PID TTY          TIME CMD
    1 ?        00:00:04 systemd
    2 ?        00:00:00 kthreadd
    3 ?        00:00:01 ksoftirqd/0
This command lists PID, TTY, TIME and process name for all processes owned by the root user.
-  We can also specify -G option and the name of an  owning group to print processes associated only with  that group
#- ps -G root
```

### Process States:

- A process changes its operating state many times during its life cycle.
- Factors such as processor load, memory availability, process priority and response from other apps affect how often a process changes from one state to another.
-Process could be in a non-running state for a while or waiting on another process to provide information so that it can continue to run.
```
- There are five basic process states: 
  - Running
  - Sleeping	
  - Waiting
  - Stopped
  - Zombie
```


### Nice Level:
assiging the priority to the process nice level starts from (-20 to 19 )where -20 is highest priority
- Each process has an assigned priority, which is established at initiation. It is based on a numeric value called niceness (or a nice value).
- There are 40 niceness values, with -20 being the highest and +19 being the lowest value.
- Most processes started by the system use the default niceness of 0. 
- A process running at higher priority gets more CPU attention.
- A child process inherits the niceness of its parent or calling process.
- Normally, we run programs at the default niceness but we can change it based on system load and urgency.
```
ps axo pid,comm,nice # this will displa nice level for each process
dd if=/dev/zero of=/root/test.file bs=1M count=1024	#this will generate the 1g file
nice -n 0 httpd #changing the nice level for httpd process but u have to stop and restart the process
renice -n 10 2879 #this command will allow us to change nice value on running process without stoping
renice -n 10 $(pgrep httpd)
time nice -n 19 tar -cvf test.tar test tar 
time nice -n -20 tar -cvf test.tar test tar
```
### Renicing a running process: 

- The niceness of a running process can be changed using the renice command. 
- Renicing will change the priority at which the process is currently running.


Example: 
```
- To change the nice of a running top session from 
old priority to +5: 
1- find the PID of top 
#- pidof crond
642 (PID)
2- Change it to +5
#- renice 5 642
3- ps -el | grep top
Note: Options -u and -g can be used with renice to  change nice values of processes owned by a user orgroup members.
```


### How to read load average

1) identify the number of cpu using cat /proc/cpuinfo
2) use uptime to check load average
3) then divde 0.38/nubmer of process

```
[root@jenkins ~]# uptime
 12:38:27 up 62 days, 19:14,  1 user,  load average: 0.38, 0.01, 0.05

0.38/2=0.19 so now we are using 19% of cpu
2.19/2=1.1 so now we are using more than 100%

```

### The top command: 
Another popular tool for viewing process info is the top command. It displays the statistics in real-time helps to  identify performance issues on the system.

Example: 

```
Tasks: 186 total,   1 running, 185 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.5 us,  4.3 sy,  0.0 ni, 95.2 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  5925684 total,  1126148 free,  1347368 used,  3452168 buff/cache
KiB Swap:  2097148 total,  1767932 free,   329216 used.  4022200 avail Mem

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
129668 root      20   0  164400   2364   1664 R   8.3  0.0   0:00.11 top
     1 root      20   0   54560   6752   4024 S   0.0  0.1  10:36.41 systemd
     2 root      20   0       0      0      0 S   0.0  0.0   0:07.87 kthreadd
     4 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0+
     6 root      20   0       0      0      0 S   0.0  0.0   8:37.29 ksoftirqd+

```

```
#: top
shift+M # will order by memory
shift+c # will order by cpu
r # renice the process by giving process pid
press q or ctrl c to quit top.
PID – Process ID
USER – Name of the effective user (owner) of the 
process.
PR – Priority
NI – Nice value
VIRT – virtual memory size
RES – resident memory size
SHR – shared memory size
S – process status (which could be one of the 
following: D (uninteruptible sleep), R (running), 
S (sleeping), T (traced or stopped) or Z (zombie)
%CPU – the share of cpu time used by the process 
since last update.
%MEM – share of physical memory used.
TIME+ – total cpu time used by the task in hundredths
of a second.
COMMAND – command name or command line 
(name + options) 

```


## Locate and interpret System Log Files and Journalctl

cd /var/log #all log files are located in this directory
tail -f -n 20 /var/log/httpd/access_log
head messages
head -n 50 <filename>


### journald
journalctl: logs all the events of the system
- journald is not persistant, wen we reboot by default jornald is removed
- journald is stored in cd /run/log/journal this is not persistant, to make persistant edit journald.conf file 
- /etc/systemd/journald.conf #config file for journald

```
journactl -n #this will show last 10 lines
journactl -xn #this will show last 10 lines with additional information
journalctl -f #this will provide last 10 lines and gives u live log
journalctl _SYSTEM_UNIT=httpd.service	#this will show the log relatid to this service
journalctl --since=yerstaday  
systemd-analyze #how much time each service has taken
```
#### rsyslog.conf #is the file which is used to create genric log file ,all logs were needs to be stored is defined in this file

# Configure Local Storage

## List,Create, & Delete  Partitions on MBR & GPT

### MBR
- MBR can have only 4 primary partiations,
- each primary partiation can be 2tb 
- MBR is 32bit based
- Used by BIOS-based systems

- /dev/ directory
- fdisk is used to manage mbr based partiation

```
1) fdisk /dev/xvdf
2) press m to select options
3) n #for new partiation 
4) p # for primary partiation
5) disk size
6)w
7) mkfs -t xfs xvdf1 #create file system on drive so that we can use the volume
8) mount /dev/xvdf1 /mtn/mymount # mount the volume on the local system in order to store the data
9) blkid #to display mounted file system
10) unmount /mnt/mymount # to unmount the mounted device 
11) partprobe  #when we write the changes os will not be able to reload the changes at that time run partprobe
run partprobe after creating,deleting & editing partation

12) u can also mount using UUID,advantage is u cannot have same uuid 
12) mount -U <UUID> /mnt/mymount
```



### GPT

- GPT can have 128 primary partations
- each partiation can have 8zb 
- 64bit
- Used by UEFI-based systems
- u can use gdisk or partprobe
```
1) gdisk /dev/xvdf
2) n  add new partiation
3) default
4) size
5) press L to check lables eg: 8300 linux file system, 8200linux swap
6) w #write partaion
7) mkfs -t xfs xvdf1 # create file system
8) mount /dev/xfdf1 /mnt/mynount #mount filesystem on the mnt/mymount
9) umount
10) blkid to c uuid

```


## LVM

LVM (Logical Volume Manager):
The LVM solution is widely used for managing disk storage.
Managing disk space has always been a significant and time consuming task for system adminstrators.

Running out of disk space used to be the start of a long and complex series of tasks to increase the space  available to a disk partition. It also required taking  the system off-line. This usually involved installing a  new hard drive, booting to recovery or single-user mode, creating a partition and a filesystem on the new hard  drive, using temporary mount points to move the data from the too-small filesystem to the new, larger one, changing the content of the /etc/fstab file to reflect the correct device name for the new partition, and  rebooting to remount the new filesystem on the  correct mount point.


LVM allows for very flexible disk space management.  It provides features like the ability to add disk space to a logical volume and its filesystem while that  filesystem is mounted and active and it allows for the  collection of multiple physical hard drives and  partitions into a single volume group which can then be divided into logical volumes.


Structure:
```
-Physical Hard drive
  - PV (Physical Volume)
     - VG (Volume Group)
	- LV (Logical Volume)
	    - Filesystem 


```
Practical Use:
```
- Create a Physical Volume:
# lsblk (To check available disks)


- Create a PV (Physical Volume)
# pvcreate /dev/sdb

- Confirm
# pvs


Create a VG (Volume Group)called test_vg on sdb
# vgcreate test_vg /dev/sdb

- To Check
# vgs
or
# vgdisplay


- Create a Logical Volume called example_lv on test_vg
Volume Group - Size of 50 MB:

- lvcreate -n example_lv -L 50M test_vg

- Check
# lvs
or
# lvdisplay /dev/test_vg/example_lv


To be able to use and mount this LV

- Create a ext3 Filesystem:

# mkfs.ext3 /dev/test_vg/example_lv


To mount this LV on a directory /tmp/example:

- Make a directory under /tmp
# mkdir example

Now mount the LV:

#  mount /dev/test_vg/example_lv /tmp/example

- Check 
# df -h

Note: This is not permanent, to make this permanent
you need to add this entry in /etc/fstab:

# /dev/mapper/test_vg-example_lv  /tmp/example ext3
defaults 1 2


Extend a Volume Group and Logical Volume:


- Add disk or use existing VG if space is available:
# pvcreate /dev/sdc
# vgextend test_vg /dev/sdc

- Check 
# vgs


- Extend a Logical Volume:

# lvextend -L 100M /dev/test_vg/example_test

Check:
#df -h
Size has not changed yet.

- Run the followinf command:
# resize2fs /dev/test_vg/example_lv

- Check again
# df -h

Success.



 To remove LV, VG and PV:

- To Remove a Logical Volume:
# unmount /tmp/exampe
# lvremove -f /dev/test_vg/example_lv


- To Remove a Volume Group:

# vgs
# vgremove test_vg

Check:
# vgs


- To remove a Physical Volume:

# pvs
# pvremove /dev/sdb

Check:
# pvs

# lsblk
see sdb as unassigned
```



























































































