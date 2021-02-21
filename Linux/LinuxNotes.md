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
The booting process takes the following 4 steps that we will discuss in greater detail:

	1. BIOS Integrity check (POST)
	2. Loading of the Boot loader (GRUB2)
	3. Kernel initialization
	4. Starting systemd, the parent of all processes

1. The BIOS Integrity Check (POST)


The boot process is usually initialized when a user presses the power-on button – if the PC was already shut down – or reboots the system using either the GUI or on the command line.

When the Linux system powers up, the BIOS (Basic Input Output System) kicks in and performs a Power On Self Test (POST). This is an integrity check that performs a plethora of diagnostic checks.


The POST probes the hardware operability of components such as the HDD or SSD, Keyboard, RAM, USB ports, and any other piece of hardware. If some hardware device is not detected, or if there’s a malfunction in any of the devices such as a corrupt HDD or SSD, an error message is splashed on the screen prompting your intervention.

In some cases, a beeping sound will go off especially in the event of a missing RAM module. However, if the expected hardware is present and functioning as expected, the booting process proceeds to the next stage.

2. The Bootloader (GRUB2)

Once the POST is complete and the coast is clear, the BIOS probes the MBR (Master Boot Record) for the bootloader and disk partitioning information.

The MBR is a 512-byte code that is located on the first sector of the hard drive which is usually /dev/sda or /dev/hda depending on your hard drive architecture. Note, however, that sometimes the MBR can be located on a Live USB or DVD installation of Linux.

There are 3 main types of bootloaders in Linux: LILO, GRUB, and GRUB2. The GRUB2 bootloader is the latest and primary bootloader in modern Linux distributions and informs our decision to leave out the other two which have become antiquated with the passage of time.

GRUB2 stands for GRand Unified Bootloader version 2. Once the BIOS locates the grub2 bootloader, it executes and loads it onto the main memory (RAM).

The grub2 menu allows you to do a couple of things. It allows you to select the Linux kernel version that you’d want to use. If you have been upgrading your system a couple of times, you might see different kernel versions listed. Additionally, it gives you the ability to edit some kernel parameters by pressing a combination of keyboard keys.

Select Kernel Version
Select Kernel Version
Also, in a dual-boot setup where you have multiple OS installations, the grub menu allows you to select which OS to boot into. The grub2 configuration file is the /boot/grub2/grub2.cfg file. GRUB’s main objective is to load the Linux kernel onto the main memory.

3. Kernel Initialization


The kernel is the core of any Linux system. It interfaces the PC’s hardware with the underlying processes. The kernel controls all the processes on your Linux system. Once the selected Linux kernel is loaded by the bootloader, it must self extract from its compressed version before undertaking any task. Upon self-extracting, the selected kernel mounts the root file system and initializes the /sbin/init program commonly referred to as init.

Kernel Initialization Process
Kernel Initialization Process
Init is always the first program to be executed and is assigned the process ID or PID of 1. It’s the init process that spawns various daemons & mounts all partitions that are specified in the /etc/fstab file.

The kernel then mounts the initial RAM disk (initrd) which is a temporary root filesystem until the real root filesystem is mounted. All kernels are located in the /boot directory together with the initial RAM disk image.



4. Starting Systemd


The kernel finally loads Systemd, which is the replacement of the old SysV init. Systemd is the mother of all Linux processes and manages among other things mounting of file systems, starting and stopping services to mention just a few.

Systemd uses the /etc/systemd/system/default.target file to determine the state or target that the Linux system should boot into.

For a desktop workstation (with a GUI) the default target value is 5 which is the equivalent of run level 5 for the old SystemV init.
For a server, the default target is multi-user.target which corresponds to run level 3 in SysV init.
Here’s a breakdown of the systemd targets:

poweroff.target (runlevel 0): Poweroff or Shutdown the system.
rescue.target (runlevel 1): launches a rescue shell session.
multi-user.target (runlevel 2,3,4): Configures the system to a non-graphical (console) multi-user system.
graphical.target (runlevel 5): Set the system to use a graphical multi-user interface with network services.
reboot.target (runlevel 6): reboots the system.
To check the current target on your system, run the command:

$ systemctl get-default
Check Run Level
Check Run Level
You can switch from one target to another by running the following command on the terminal:

$ init runlevel-value
For example, init 3 configures the system to a non-graphical state.

The init 6 command reboots your system and init 0 powers off the system. Be sure to invoke sudo command when you want to switch to these two targets.

The booting process ends once systemd loads all the daemons and sets the target or run level value. It’s at this point you are prompted for your username and password upon which you gain entry to your Linux system.



### boot process v2
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

- physical volume, each lvm has underlying physcal volume, it can be a partiation volume or entier disk
- we have to initilize physical volume as physical volume for lvm, by doing this lables place on first part of the volume(metadata) helps to identify physical volume for LVM,
- its place in 2nd 512 byte sector on physical volume
- u can have either 0,1 or 2 copys of metadata  
- by default 1 copy is stored on physical volume
- once number of copys is configured you cannot change number of copies avilable
- 1st copy is stored in 1st of the device and 2nd copy is stored at end of device thus it protects accedental override

we have pv,vg,lv,
vg is combination of physical volumes that creates a pool of space that the logical volume manager or logical volumes can allocate.
its made of extents now extent is insde a VG
- It's the disk space that's provided inside of locatable fixed units are called extents and extent 
- the smallest unit of space that can be assigned to a volume group volume group extents are referred
- VG Extents are definced physical extents and Logical volume is allocated in two sets on logical extents that are same size as physical extents that maps to it
- LV extents is mapped to the PV extents and that is how the logical volume communicates to physical volume data
- we can use entire disk for lvm ,to use lvm we have to ctrete file system wit lable LVM for everythin to work perfectly 


```
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
step1: create lvm lable for partation
1) gdisk xvdf
2) n
3) 8e00
4) y 
5) w
step2: create physical volume
6) pvcreate /dev/xvdf1 /dev/xvdvg1
7) pv display
step3: create volume group: vg is made up of PV
8) vgcreate battlestar_vg /dev/xvdf1 /dev/xfdg1
9) lvcreate -n galactica -L 10G battlestar_vg		#creating lv using size
9) lvcreate -n galactica -l 100	battlestar_vg	#creating lv using PE extens
10) lvdisplay
step 4: create filesystem on lvm
11) mkfs -t xfs galactica
12) mount /dev/battlestar/galactia /mnt/mymount  


note: xfs filesystem only can be increased not decreased
ext4 can be increase and decreased


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



- To remove a Physical Volume:

# pvs
# pvremove /dev/sdb

Check:
# pvs

# lsblk
see sdb as unassigned
```


## Configure system to mount file system at boot using UUID


```
step 1: create partaion
step 2: creat lvm label,pv,vg lvm
step 3: crete filesystem
step 4: mount filesystem

blkid
use the uuid and place that in fstab
/etc/fstab
```

What is fstab?
- Fstab is your operating system’s file system table
- Fstab is configured to look for specific file systems and mount them automatically in a desired way each and every time, preventing a myriad of disasters from occurring.
- mount -a #this command will mount all the disk avilable on fstab 
- umount -a # this command will unmount all disk which r in fstab
```
#
# /etc/fstab
# Created by anaconda on Mon Mar 18 23:09:13 2019
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=3a25124f-7cc7-4a83-bd0e-b7587bda5b65 /boot                   xfs     defaul            ts        0 0

/dev/mapper/centos-swap swap                    swap    defaults        0 0
#/dev/mapper/test_vg-test_lv   /root/example     ext3    defaults        1 2

```
As you can see from the output above, each line consists of six fields. Here is a description of each of them:

1) Device – the first field specifies the mount device. These are usually device filenames. Most distributions now specify partitions by their labels or UUIDs.
2) Mount point – the second field specifies the mount point, the directory where the partition or disk will be mounted. This should usually be an empty directory in another file system.
3) File system type – the third field specifies the file system type.
4) Options – the fourth field specifies the mount options. Most file systems support several mount options, which modify how the kernel treats the file system. You may specify multiple mount options, separated by commas.
5) Backup operation – the fifth field contains a 1 if the dump utility should back up a partition or a 0 if it shouldn’t. If you never use the dump backup program, you can ignore this option.
6) File system check order – the sixth field specifies the order in which fsck checks the device/partition for errors at boot time. A 0 means that fsck should not check a file system. Higher numbers represent the check order. The root partition should have a value of 1 , and all others that need to be checked should have a value of 2.

## Adding New Partations and logical volumes and swap to a system Non Default

### understanding swap memory

- Swap is a space on a disk that is used when the amount of physical RAM memory is full. When a Linux system runs out of RAM, inactive pages are moved from the RAM to the swap space.
- Swap space can take the form of either a dedicated swap partition or a swap file. In most cases, when running Linux on a virtual machine, a swap partition is not present, so the only option is to create a swap file.
- swap space size should be 2 or 2.5 times of memory

Creating Swap Partition
```
step 1) 
a) fdisk xvdf
b) n
c) p
d) 8e #create lvm label
e) w
step 2) 
a) pvcreate /dev/xvdf1
b) vgcreate battelstar /dev/xvdf1
c) lvcreate /-n swap -L 2G battlestar
Step 3) now we have lvm now we have to prepare lvm as swap so to do that we need to format to swap signature

a) sudo mkswap /dev/battlestar/swap #format to swap signature
b) sudo swapon /dev/battlestar/swap  # this command will mount all the swap entries on fstab file
c) sudo swapoff /dev/battlestar/swap
d) to make it permenant add it in fstab
/dev/battlestar/swap swap swap defaults 0 0 # add this in /etc/fstab
e) sudo swapon --show



sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
# Add the following on fstab
/swapfile swap swap defaults 0 0 # add this in /etc/fstab
sudo swapon --show
sudo swapoff -v /swapfile
sudo rm /swapfile
```


# Create and Configure File System

## Create Mount Unmount and use VFAT EXT4 & XFS file system

- VFAT: Stands for "Virtual File Allocation Table." Older Windows operating systems (Windows ME and earlier) used a file system called "FAT" or "FAT32." The file system is what the operating system uses to organize and access files on the hard drive. VFAT, introduced with Windows 95, was an improvement to the basic FAT file system, allowing more information to be stored for each file. While the FAT file system can only store 8 characters for each file name, VFAT allows for file names up to 255 characters in length. Personally, I use the term VFAT to refer to the size of my cat.
- its extend version of fat file system created by microsoft
- one reson to use vfat is, if u want to share linux machine drive on window machine then u can use vfat

```
mkfs.vfat /dev/xvdf1
mkdir /mnt/vfat
mount /dev/xvdf1 /mnt/vfat
#add this in fstab
/dev/xvdf1 /mnt/vfat vfat defaults 1 2
fsck
``` 

EXT4
```
mkfs.ext4 /dev/xvdf1
mkdir /mnt/ext4
mount /dev/xvdf1 /mnt/ext4
#add this in fstab
/dev/xvdf1 /mnt/ext4 ext4 defaults 1 2

note: fsck cannot check on mounted file system so to run fsck you have to unmount 
umount /mnt/ext4  
fsck /dev/xvdf1 
dumpe2fs /dev/xvdf1
tune2fs -L ext4_label /dev/xvdf1  # creates lable and u can use this lable on fstab
and also gives indoes details
```

XFS: it has high throughput,500tb
```
mkfs.xfs /dev/xvdf1
mkdir /mnt/xfs
mount /dev/xvdf1 /mnt/xfs


```

## Mount and Unmount CIFS and NFS

- CIFS: Common Internet File System (CIFS) is a network filesystem protocol used for providing shared access to files and printers between machines on the network
cifs are mainly used on windows based os,
SAMBA used cifs

samba
```
yum install cifs-utils
smbclient -L <server-ip>
mount -t cifs -o username=<username> //<server-ip>/<share-name> /mnt/sambashare
add share in fstab for permenant mount
//10.0.0.100/public /mnt/sambshare cifs username=<>,password=<>
```
- NFS: NFS (Network File System) is basically developed for sharing of files and folders between Linux/Unix systems by Sun Microsystems in 1980. It allows you to mount your local file systems over a network and remote hosts to interact with them as they are mounted locally on the same system

- Creating NFS


Downloading and Installing the Components
```
ON SERVER
	sudo apt-get update
	sudo apt-get install nfs-kernel-server
ON CLIENT
sudo apt-get update
sudo apt-get install nfs-common
```
Creating the Share Directory on the Host Server
```
sudo mkdir /var/nfs
sudo chown nobody:nogroup /var/nfs
```
Configuring the NFS Exports on the Host Server
```
sudo nano /etc/exports
/home 192.168.0.101(rw,sync,no_root_squash,no_subtree_check)
/var/nfs 192.168.0.101(rw,sync,no_subtree_check)
	
```

Defination of rw,sync,no_subtree_check

```
Let us now take a while to understand the options given in the lines above.

rw: This option allows the client computer read as well as write access to the volume.
sync: It forces NFS to write changes to the disk before replying, thus resulting in a more stable and consistent environment. This is primarily because the reply replicates the actual state of the remote volume.
nosubtreecheck: This option averts subtree checking, which is a process that compels the host to check if the file is actually still available in the exported tree for each request. It may create problems when a file is renamed while the client has it opened. For the same reason, in roughly all the cases, it is advisable to disable subtree checking.
norootsquash: By default, the NFS translates requests from a root user remotely into a non-privileged one on the server. This is meant to be a security feature that does not allow a root account on the client to use the filesystem of the host as root. This kind of a directive disables this for a certain lot of shares.
```
sudo exportfs -a
```
yum install nfs-utils
mount -t nfs -o <server-ip>: <share-name> /mnt/sambashare
add share in fstab for permenant mount
//10.0.0.100:/public /mnt/sambshare nfs defaults 0 0 
```
## Extending Existing LVM

- Create New partation
- 

MBR Based Partations
```
fdisk xvdf
 n
 p
 default
 8e #lablel
create physical volume
pvcreate /dev/xvdf1
pvdisplay
vgcrete battelstar /dev/xvdf1
# now we have volume group
lvcreate -n galactica -L 1G battlestar
mkfs -t xfs /dev/battestar/galactica
mkdir /mtn/myvol
mount /dev/battelstar/galactica /mnt/myvol
creat file for testing file1 and file2
# now we have one device where file1 and file2 exists  now if u want to change for mbr based partation to gpt based paratin
but i dont want to data to get deleted so we use lvm

# now we will create gpt based partation 
gdisk xvdg
  n
 p
 default
 8e00 #lablel
 w
pvcreate /dev/xvdg1
pvdisplay
# now we have created one more partation now we have to added this volume to volume group

vgextend battlestar /dev/xvdg1
#now i want copy all the data in xvdf1 to xvdg1 we can do this as long as there is free space

pvmove /dev/xvdf1 #this will move 

# reducing vg
vgreduce battlestar /dev/xvdf1
	

lvextend -L 5G /dev/battlestar/galactica #this will add totol volume of 5g
lvextend -L +5G /dev/battlestar/galactica # this will add additional volume of 5g
# after extending lvm size of mount will not be updated
resize2fs /mnt/myvoulem # for ext based device
xfs_growfs /mtn/myvolume # for xfs this will reinitilized the size
```



Extend a Volume Group and Logical Volume:
```
Step 1)
- Add disk or use existing VG if space is available:
# pvcreate /dev/sdc
# vgextend test_vg /dev/sdc

- Check 
# vgs or vgdisplay

Step 2)
- Extend a Logical Volume:

# lvextend -L 100M /dev/test_vg/example_test

Check:
#df -h
Size has not changed yet.


Step 3)

- Run the followinf command:
# resize2fs /dev/test_vg/example_lv
- Check again
# df -h

Success.

Step 4)
 To remove LV, VG and PV:
- To Remove a Logical Volume:
# unmount /tmp/exampe
# lvremove -f /dev/test_vg/example_lv

Step 5)
- To Remove a Volume Group:
# vgs
# vgremove test_vg

Check:
# vgs

```

## Create and Configure Set-GID Directories fo rcollabaration

- when ever your creating files primary group will be logined user group this will create problem duraing collabration work
```

mkdir finance
touch file1
#file1 will have root user group as primary group so another user will not be able to access this file in the same finance group

SETGID: this all files created inside of the directory that has the set GID on it will obtain or inherit the permissions of parrent directory
chmod g+s finance # this will set the sgid bit for this fill
chown :finance  finance # change group owner of the file to finance
```

## Create and Manage Access Control Lists(ACL)

What is ACL ?
- Think of a scenario in which a particular user is not a member of group created by you but still you want to give some read or write access, how can you do it without making user a member of group, here comes in picture Access Control Lists, ACL helps us to do this trick
- Access control list (ACL) provides an additional, more flexible permission mechanism for file systems. It is designed to assist with UNIX file permissions. ACL allows you to give permissions for any user or group to any disc resource.
- acls are built for granular level permission
- not all filesystem supports ACL, only xfs and EXT4 supports ACl's
Use of ACL :
- setfacl and getfacl are used for setting up ACL and showing ACL respectively.
- setfacl can be assigned to groups and users
- if u change chmod on file the same will be updated to file this is called minimum acl entries
- chmod dosnet necessarly modify the acl, it modfies the mask 
- mask #say that maximum level permission for the file, even if user has permisson if mask entry is 000 the user will be denied to access the file
- + sign (ls -l) indicates that particular files has acls


```
setfacl -m u:<username>or<user-id>:rw file1 #wher "u" is for users
setfacl -m m::r file #modifing the mask 
setfacl -m g:<groupname>or<group-id>:rw file1 #wher "g" is for group
chmod will update the mask
```
ACL Defaults: its the acl which is assigned during  directory creation

```
setfacl -d -m u:starbuck:rwn dir1 #creating default acls for the directory, if we try to create the file inside directory then u ll get error coz starbuck user has only default 
permission not user permission so now assign user permission(setfacl -m u:starbuck:wr dir1) 
setfacl --remove-default dir1 # removing default permission of directory
setfacl -x d:u:starbuck dir #removing regular user permission of directory
setfacl -x d:g:starbuck dir #removing regular group permission of directory

```

## Diagnose and correct file permission Problems
we cannot delete a file
- update the acl on the file or directory Mask
- group acl
- directorys need to have execute permission so that can have read permsision -X
- cp command dosnet preserve ACL rules
- mv command does preserver acl rules


# Deploy Configure and Maintain Systems

## Configure Networking and Hostname Resolution statically or Dynamically

```
ping 
ip addr show eth0
tracepath <ip>
traceroute <ip>
netstat 
ss -at #it shows ip address listening on
ss -atn # to c port number, which port listening
ip -s link show eth0 #show static info of eth0 

``` 

## Network/Hostname

Basic Network components you must know:
```
IP Address
Subnet Mask
Gateway
Static vs DHCP
Ethernet and Virtual Interface
MAC Address

```

IP Address: An Internet Protocol address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
Most networks today, including all computers on the  Internet, use the TCP/IP protocol as the standard for  how to communicate on the network. In the TCP/IP  protocol, the unique identifier for a computer is  called its IP address.

There are two standards for IP addresses:  IP Version 4 (IPv4) and IP Version 6 (IPv6). All computers and networked devices with IP addresses have an IPv4 addressand many are starting to use the new IPv6 address systemas well.

IPv4:

IPv4 uses 32 binary bits to create a single unique address on the network. An IPv4 address is expressed by four numbers separated by dots.Example: 192.168.123.132

Each number represents eight-digit binary number, also  called an octet. These eight bit sections are known as octets. 
The example IP address, then, becomes 
11000000.10101000.01111011.10000100
192     .168     .123     . 132 

IPv6:
When the Internet exploded, IPv6 was created as it was realized that we may run out of IPv4 addresses. IPv6 uses 128 binary bits to create a single unique  address on the network. 
An IPv6 address is expressed by eight groups of  hexadecimal numbers separated by colons:
2001:cdba:0000:0000:0000:0000:3257:9652
Groups of numbers that contain all zeros are often  omitted to save space:
2001:cdba::3257:9652



- Subnet Mask and subnetting:The practice of dividing a network into two or more  networks is called subnetting.

For IPv4, a network may also be characterized by its  subnet mask or netmask.
```
For example: 255.255.255.0 is the subnet mask for the 
prefix 198.51.100.0/24.
```

- Gateway: A gateway is a network node that connects two networks using different protocols together. While a bridge is  used to join two similar types of networks, a gateway is used to join two different networks.

Common Gateway is your home modem or your router.

- Static IP vs DHCP or Dynamic IP: A Static IP address is a dedicated IP address that does not change. This is an IP address that is used by your  system every time you log in to the network. 
DHCP or Dynamic is an IP address that will automatically be chosen for you from a pool of IP addresses that are  assigned in the DHCP scope available on your network. Think Static as permanent and DHCP as temporary IP.



Ethernet and Virtual Interface

- Ethernet Interface: This usally the NIC (Network Interface card) that is on that back of your computer a.k.a. NIC Card.

- Virtual Interface: Very common now in Virtual environments such as Oracle VM virtualbox, VMWare etc.  Virtual interfaces exist only in software; there are no physical elements. You identify an individual virtual  interface using a numerical ID after the virtual  interface name such as eth0.


MAC address: Every NIC virtual or physical has a hardware address  that's known as a MAC. MAC stands for Media Access Control, and each identifier is intended to be unique to a particular device.

A MAC address consists of six sets of two characters,  each separated by a colon:
```
Example:
00:1B:44:11:3A:B7
```

### 
Hostnamectl #this will update the hostname file
hostnamectl set-hostname <hostname>
hostnamectl status

## Schedule Task AT and Cron

### Understanding Job scheduling: 

- Job scheduling allows a user to submit a command or a program for execution at a specified time in the future.
- The execution of the command or program could be one time or recurring based on pre-determined time schedule.
- One time execution is normally scheduled for an  activity that needs to performed at low system usage times. For example, an execution of a lengthy shell program.
- In contrast, recurring activities may include backups, deleting old log files, system monitoring tasks,  running custom scripts and removing unwanted files.



- Job scheduling and execution is taken care of by two daemons: 
	a) atd
  	b) crond

atd:  atd manages the jobs scheduled to run one time in the future. The atd daemon retires a missed job at the same time next day.

Scheduling with at command: 

The at command is used to schedule a one-time job in the future.

All submitted jobs are spooled in the /var/spool/at directory and executed by atd daemon at specified time.

This file also includes the name of the command or script to be run.


Ways of expressing a time with the at command: 
```
at 1:20am    =  Runs at next 1:20am
at noon	     =	Runs at 12pm
at 12:42     = 	Runs at 11:42pm
at midnight  = 	Runs at 12am
at 17:01 tomorrow  =  Runs at 5:01pm, next day.
at now + 7 hours  = Runs 7 hours from now
at 3:00 1/15/2019 = Runs at 3am on Jan 15, 2019
```
You can also supply a filename with at command using  the -f option. This command will execute that file at specified time

Submit, view, list and remove an at job:


Exerice:
```
1- Run the at command and specify the time and date for the job execution.
# at 11:30pm 6/30/2019
at> find / -name core #press ctrl+d


2- List the job file created in /var/spool/at:

# ll /var/spool/at
ID 5 created for job

3- Display contents of this file:
# cat /var/spool/at/file
 or
# at -c 5

4- List spooled job:
# at -l or atq

5- Remove spooled job
# at -d 5 or  atrm 5

6)loging at
at teatime 	#this will execute at teatime 4pm
at> logger "log file" <EOT>

for log c journalctl -q
This will remove the job file from /var/spool/at. Can be confirmed with atq command as well.
ls etc|grep at #u can find at files
at.deny: if user is present in at.deny file then user will not be able to access at
at.allow: if at.allow exist then all user are not allowed, unless its specfied in this file 
atq	#to display the jobs
at.deny   #if user is specfied in this file the user is not allowed u to use at command
at.allow  #all user execpt the user specfied in the file do not have permission to execute at command
if at.allow file exist then the user which is specfied in this file is only allowed to use at commands
journalctl -xn # to c job executed status 

```
### Cron
- crond: crond manages recurring jobs at pre-specified times. At startup, this daemon reads schedules in files  located in the /var/spool/cron and /etc/cron.d directories and loads them in the memory for later execution.
This daemon run a job at its scheduled time only and unlike atd daemon does not entertain missed jobs.
- if system is down cron will not be executed were as at will be executed
- Note:  Neither daemon needs to restart after any additions or changes.
- cron is linked with anacrontab /etc/abacrontab,daily,weekly --etc are specfied in this file



Crontab: Using crontab is another method of scheduling jobs to in the future. 

ls /etc/cron* # it contains cron.daily ,weekly mothly directory, u can place the scripts in particular directory to execute automaticaly

Unlike, atd, crond executes cron jobs on a regular basis as long as they comply with format defined in the /etc/crontab file.

#- cat /etc/crontab

Crontables for users are located in the /var/spool/cron directory. Each authorized user with a scheduled job has a file matching their user name in this directory.

For example: 

The crontab file for User1 will be: /var/spool/cron/user1 

Crontables are also stored in /etc/cron.d directory,  only root user has access to create, modify and delete them.
When daemon is done running the jobs at the specified  time, it adds a log entry to /var/log/cron file.


- To check if cron is already installed:
```
# yum list installed | grep cron   or # rpm -qa | grep cron


Crontab command can be used with options:
-e = to edit
-l = to list
-r = remove crontables
```

Syntax of User Crontab Files:
```
The /etc/crontab file specifies the syntax that each cron job must comply with.

cat /etc/crontab

Field	Description	Allowed Value
MIN	Minute field	0 to 59
HOUR	Hour field	0 to 23
DOM	Day of Month	1-31
MON	Month field	1-12
DOW	Day Of Week	0-6
CMD	Command	Any command to be executed.
```


Example: 
```
- Scheduling a Job For a Specific Time The basic usage of cron is to execute a job in a  specific time as shown below. This will execute the  Full backup shell script (full-backup) on 11th July  at 09:30 AM.

Please note that the time field uses 24 hours format. So, for 9 AM use 9, and for 9 PM use 21.

1- # crontab -e
2- Add the below line:
30 09 11 07 * /home/user1/full-backup
-------------------
30 – 30th Minute
09 – 09 AM
11 – 11th Day
07 – 7th Month (July)
* – Every day of the week
-------------------
```
```
crontab -l  #To check the contents of crontable.
```
Add list and remove a Cron job:
- Add a cron job as user 'test':
crontab -e #Edit crontab file: 

30 09 11 07 * /home/test/script # Add your job in file:

3- Save an exit.
Note:
This will execute the  script (full-backup) on 
11th July at 09:30 AM.

crontab -l #List contents of crontable:
crontab -r # Remove a cronjob as user test:



## Start & Stop Services

```
systemctl start <service>
systemctl stop <service>
systemctl status <service>
systemctl enable <service>
systemctl disable <service>
systemctl list-unit
systemctl get-default
systemctl list-dependencies multi-user.target	
```
## configure system to boot into specfic targets

kickstart server

kickstart.cfg
yum install system-config-kickstart 	#this will start gui based kickstart config tool


## Configure system to boot in specfic target

```
systemctl get-default
systemctl set-default graphical.targett
reboot
```

## Time Services

timedatectl: this command provides system time date 

```
timedatectl set-ntp true #ntp enaled
timedatectl set-ntp false # ntp is disabled
timedatectl list-timezone #this will list the time zone, if ur not familar with timezone then u can use tzselect
tzselect: # this will help u identify the time zone
timedatectl set-timezone america/chicago
date # view current date time
```
### NTP
ntp: by default ntp use chronyd deamon,

```
systemctl status chronyd
yum install chrony
chronyd			#ntp deamon
chronyc sources -v 	#to get list of servers that communicate to get time
```
chronyc sources -v
```
Number of sources = 4

  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current synced, '+' = combined , '-' = not combined,
| /   '?' = unreachable, 'x' = time may be in error, '~' = time too variable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^- static.15.192.216.95.cli>     2  10   377   988  -5434us[-5454us] +/-   94ms
^* 139.59.55.93                  2  10   377   445   -109us[ -131us] +/-   31ms
^- mail.deva-ayurveda.eu         2  10   377   733    -57ms[  -57ms] +/-  131ms
^- 43.240.66.74                  4  10   377   672  +2968us[+2947us] +/-  115ms
```

- startum: number of hops it takes to reach master server in order to get the time details, lower the number better 
- * indicated currently source its synced with
-  chronyc tracking # this command will display more info about time sysncing
- /etc/chrony.conf # chrony setting file be located here, all the servers were it need to sycned is mentioned in this file



## Install and update software pacakges YUM repo
Introduction: 

- Linux applications are called Packages. A software package is a group of files organized in a directory structure and metadata that makes up a software  application. 
- Files contained in a package include installable scripts configuration files, library files, commands and the related documentation. 
- The Redhat software management system was originally called Redhat Package Manager but is now known as RPM Package Manager (RPM). 



- insted of updating all packages , check package need to be update and update the same 
```
yum search apache #this will searcgh for apache
yum seaech all #  
yum install <package>
yum list installed #to list all package installed  
yum list installed http #dispaly packgae installed
yum provides /var/www	#to check which package created this directory
yum list all #this will list all pakcage avilable on repo and installed
yum remove <package> # to remove package
yum clean all #this will clean all temp file related to repo
yum repolist all
yum-config-manager --add-repo=<repo>
yum-cionfig-manager --disable jenkins
yum-config-managet --enable jenkins
```

## Install and update software package RPM

### Redhat Subscription Management Service (RHSM): 

- This is a service provided by Redhat. You first register your systems with RHSM then attach subscriptions to them based on the OS and and software they run.
- Once registered through RHSM your system is entitled to software updates, technical support and access to the  supported software. 
- Note: CentOS is the same thing as Redhat but without the support from Redhat.



- Registering you system with RHSM: 

```
subscription-manager register --auto-attach

Username
Password
System has been registered
Status: Subscribed
```


- Unregistering and unsubscribing your system with RHSM:
 
```
# subscription-manager remove --all
# subscription-manager unregister
# subscription-manager clean
```



### We can use RPM to install, remove and manage packages.
- you can use yumdownloader to download rpm package from repo
- yumdownlader nano #this will download the rpm package
Example:
```
rpm -ivh <package name> ## i for install, v for verbose h to show progress bar
rpm -qa | grep ssh	# to query the package	
rpm -qa 		# to query the package
rpm -ql	<package name>	# this will query package and l is for list pacakge		
rpm -e 	<package name>	# to remove package
```
## Managing Repositories
if 3rd party reop is not avilable on rpm then u can add the repo config file in /etc/yum.repos.d , in this u can find repo config files
 
```
yum-config-manager --add-repo=<repo> #this will add the repo
yum-cionfig-manager --disable <repo name> #disabling repo using config manager or u can do by edit repo file "enabled=0"
yum-config-managet --enable jenkins


[epel]
name=Extra Packages for Enterprise Linux 7 - $basearch   				#package name
#baseurl=http://download.fedoraproject.org/pub/epel/7/$basearch				#URL
metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-7&arch=$basearch&infra=$infra&content=$contentdir 
failovermethod=priority
enabled=1		# enable or disabled
gpgcheck=1		# verfiys the certificate
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 #gpg key file 

```
## Configuring Local Repo
#### local repo , how to use dvd iso repo

```

setp1: mount -o loop rhel-server-7.1.x86_64-dvd.iso /repos/local  #mount the dvd iso 
step2: 			#extract from dvd
step3: create local-repo
[local-repo]
name=red hat linux local repo
baseurl=file:///repo/local
enable=1
gpgcheck=0
```
## gpgkey is importat so that u can verfiy the repo is valid repo
```
- how do you know that a specific package that you're downloading from the repository is actually verified and signed by the repository in is authentic. For some reason maybe there's an opportunity for a man in the middle attack
- GPG keys allow us to take the public varified key sign it again store verify the signature against the GPG key and the repository for the package. That way whenever we download the package it ensures that it's coming from the repository and that packag



yum-config-manager --add-repo <repo url>
open the url and find the gpg key
go to /etc/pki/rpm-gpg 
not download the gpg key in this directory
copy the url and past in /etc/yum.repo.d/<repo>gpgkey=file////
```
## update the kernal package
```
uname -r
yum install kernal 
yum clean
yum list kernal		# showl liist of installed and update kernal 

installing kernal using rpm
yumdownloader kernel
yum install linux-firmware
rpm -ivh kernal
```

## changing diffrent kernel, modifiy the bootloader to point to diffrent kernel 	

```
step1:yum list kernel	#check for list of kernel avilable	
step2: grug2-set-default 0 or 1 or 3 #by default 0 is most recent version 

```

# Manage Users & Group
## create delete and modifiy the user

```
- each user will have user id (uid,gid,groups,selinux context)
- root user has id=0
- id from 1 to 200 is system user
- 201-999 Those are for System users that use system processes but don't own files on the system eg: appache 



```
#### /etc/passwd file format
	tom:x:1000:1000:Vivek Gite:/home/vivek:/bin/bash


1. Username: It is used when user logs in. It should be between 1 and 32 characters in length.
2. Password: An x character indicates that encrypted password is stored in /etc/shadow file. Please note that you need to use the passwd command to computes the hash of a password typed at the CLI or to store/update the hash of the password in /etc/shadow file.
3. User ID (UID): Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups.
4. Group ID (GID): The primary group ID (stored in /etc/group file)
5. User ID Info: The comment field. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command.
6. Home directory: The absolute path to the directory the user will be in when they log in. If this directory does not exists then users directory becomes /
7. Command/shell: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. Please note that it does not have to be a shell. For example, sysadmin can use the nologin shell, which acts as a replacement shell for the user accounts. If shell set to /sbin/nologin and the user tries to log in to the Linux system directly, the /sbin/nologin shell closes the connection.

### Cat /etc/shadow
	thiru:!!:18488:0:99999:7:::

```


Username : It is your login name.
Password : It is your encrypted password. The password should be minimum 8-12 characters long including special characters, digits, lower case alphabetic and more. Usually password format is set to $id$salt$hashed, The $id is the algorithm used On GNU/Linux as follows:
	    $1$ is MD5 ,$2a$ is Blowfish ,$2y$ is Blowfish ,$5$ is SHA-256 , $6$ is SHA-512
Last password change (lastchanged): Days since Jan 1, 1970 that password was last changed
Minimum  : The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
Maximum  : The maximum number of days the password is valid (after that user is forced to change his/her password)
Warn     : The number of days before password is to expire that user is warned that his/her password must be changed
Inactive : The number of days after password expires that account is disabled
Expire   : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.
```
/etc/login.def

- useradd command will have lot of option u no need to mention each and every options, default values are specfied in login.defs file eg: home_directory,umask,pass max days...etc

/etc/default/useradd # in this file contains default values
```
# useradd defaults file
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/bash
SKEL=/etc/skel
CREATE_MAIL_SPOOL=yes

```

useradd

```
id

useradd thiru 
usermod -U thiru
usermod -u <user-id> thiru #to change user id
useradd -u 1050 -d /home/thiru
userdel -r or -f #this will remove the user
/etc/default/userdd		#this file consist of default value for user like(group,home,inactive,expire,shell,skel,create_mail_spool)



```
## Change Password and Adjust Password Aging for local user

- /etc/login.def #this file allow us to set particular default for passowrd 
eg:
```
..
# Password aging controls:
#
#       PASS_MAX_DAYS   Maximum number of days a password may be used.
#       PASS_MIN_DAYS   Minimum number of days allowed between password changes.
#       PASS_MIN_LEN    Minimum acceptable password length.
#       PASS_WARN_AGE   Number of days warning given before a password expires.
#
PASS_MAX_DAYS   99999
PASS_MIN_DAYS   0
PASS_MIN_LEN    5
PASS_WARN_AGE  
..

```
/etc/shadow #this fill contains the info wen passwd gona expire, wen to change..etc

/etc/shadow

```
thiru:!!:18488:0:99999:7:::

Username : It is your login name.
Password : It is your encrypted password. The password should be minimum 8-12 characters long including special characters, digits, lower case alphabetic and more. Usually password format is set to $id$salt$hashed, The $id is the algorithm used On GNU/Linux as follows:
	    $1$ is MD5 ,$2a$ is Blowfish ,$2y$ is Blowfish ,$5$ is SHA-256 , $6$ is SHA-512
Last password change (lastchanged): Days since Jan 1, 1970 that password was last changed
Minimum  : The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
Maximum  : The maximum number of days the password is valid (after that user is forced to change his/her password)
Warn     : The number of days before password is to expire that user is warned that his/her password must be changed
Inactive : The number of days after password expires that account is disabled
Expire   : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.

user add user1
passwd 
usermod -s /sbin/nologin  thiru #changing user to nologin, user will not be able to login to shell
usermod -e 			#wexperiation date
chage -l <user>		#will display the passwd details 
chage -E		#EXPERATION

```

## creating goup
```
groupadd # to create new group
getent group #list all groups in the system
cat /etc/gshadow	#to view group details
getent group thiru	#it returns all of the group the user belongs to
groups <users>		#displays primary and supplimentry group
usermod -g <primary grou> <user> # this will change primary group of user
groupmod -n		#to change the group name etc
groupmod -g		#to chage group id
groupdel <group>	#deleteing group u cannot the delete the group which is primary to another user
```
## Set Gid / SGID


when ever user create a file in group directory then if file has his own permission then other will not be able to access it so, in order to over come this we use sgbit when sbit is set file inherites the parrent directory permission 
```

dhmod g+s <directory>
#configure system to use existing authentication
connecitng for single sign on	
```
## connecting ad to linux

	yum install realmd 

## Configuring Firewalls settings using Available Firewall Utility


	yum install firewalld firewall-config
	systemctl start firewalld
	systemctl enable firewalld

	firewalld has two type 
	1) runtime changes: changes made at this level(run level change) will not be
	 persistant after reload or reboot,dosent requried reload, 
	2) To make persistant use --permanent and the --reload firewall

```
firewall-cmd
firewall always groups inside a zone,each zone can be configured 
firewall-cmd --get-zones #to get list of zones, we are alway in spefic zone 
firewall-cmd --get-default-zone # to get default zone
firewall-cmd --zone=home --add-source=192.168.0.0/24 # not persistant
firewall-cmd --zone=home --permanent --add-source=192.168.0.0/24 #persistant
firewall-cmd --zone=public --permanent --add-port=80/tcp
firewall-cmd --reload
firewall-cmd --list-all
firewall-cmd --set-default-zone=internal
firewall-cmd --get-default-zone
firewall-cmd --list-all-zones
firewall-cmd --set-default-zone=internal
firewall-cmd --get-default-zone

firewall-cmd --get-zone-of-interface=enp0s3  #To check zone in which interface is bounded
```

- Services are set of rules with ports and options which is used by Firewalld.  Services which are enabled, will be automatically loaded when the Firewalld service  up and running. By default, many services are available, to get the list of all  available services, use the following command.

```
cd /usr/lib/firewalld/services/		# To get the list of all the default available services,

firewall-cmd --get-service
firewall-cmd --add-service=rtmp
firewall-cmd --zone=public --remove-service=rtmp
firewall-cmd --add-service=rtmp --permanent
firewall-cmd --reload
firewall-cmd --permanent --add-source=192.168.0.0/24
firewall-cmd --permanent --add-port=1935/tcp
firewall-cmd --reload 
firewall-cmd --list-all
```
### Adding Rich Rules for Network Range
```
firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="http" accept' 
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="http" accept' --permanent

 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="https" accept'
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="https" accept' --permanent

 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="vnc-server" accept'
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="vnc-server" accept' --permanent

 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="postgresql" accept'
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="postgresql" accept' --permanent
```

## selinux
```
getenforce
setenforce
cd /etc/selinux
ls -Z			#will display context
use Z to display the selinux context
pa auxZ
restorecon index1.php		#use this it resotre the context on the file/folder

by default wen u configure selinux all file system are labeld, if u want to force a relable file/directory u need to make 
sure the .autorelable is present in root directory
semanage fcontext -l	#waht context 
chon #to set context manually
semanage fcontext -a httpd_sys_conten_t '/content(/.*)?'		#-a means add , -t for type type context,


```

## LOG ROTATE
```
logrotate is designed to easy admin of systems that generate large number of log files.
normaly logrotate is run as cronjob that is daily /etc/cron.daily
logrotate can done based on follwoing criteria
1)based on log file size
2)time base log rotation
3)compress old log files
4)clean log files which are matching log rotation rule
5)create new files after log rotate


cat /etc/cron.daily/logrotate		#logrotate script
/etc/logrotate.d			#logrotate file will be in this loctaion

if u want create a custom logrotate script then u can create script and place it in /etc/logrotate.d
**
/tmp/log/*.log{
	create 0644 root	#set owner permission
	daily			#Running daily
	missingok		#if no log file then dont rise ny error
	rotate 4		#keep 4 log files
	compress		#compress log file
	notifempty		#if log file is empty then dont rise erro
	postrotate		#after rote run this script
		/scripts/backuplog.sh	
	endscript
}

to execute created file 
logrotate -f /etc/lograte.conf

```

##epel repositary

##recovery deleted files on linux
```
testdisk #is free datarecovery software 
VI

press following in command mode
#d to delete the line
#y copy the line	
# shift+g		#to navigate to top
# shift+G		#to navigate to bottom
# cc will remove the line and will go to insert mode


```
# Linux Interview Questions

Linux qs

```
Q)top and ps?
Q)how will u check dependencies lis of packages? Ans: yum deplist mysql
Q)what is dhcp
Q)diffrent bw rpm yum: dependency
Q)To enable auto mounting in client side : Autofs
Q)to get fixed ip in dhcp we must set "fixed-address"
Q)to run command in bacground us ampresent sign &
Q)remove user from group: usermod -d <uname> <group name>
2)what is firewall: it moniters incoming and outgoing packets and controls the packet
3)what is selinux, selinux context?
Q)what is log managment?
Q)explaing process states
Q) viewing Inode : ll -i , stat <filename>
q) total number of inodes avilable :  df -i
q)To check how many inodes you will have, use

```
mkfs.ext4 -n /dev/sda

D uninterruptible sleep(Usally IO)
I idle kernel thread
R running or runnalbe
S intrruptible sleep
T Stopped by job controll
t

Q)what is dns
```
https://medium.com/@maneesha.wijesinghe1/what-happens-when-you-type-an-url-in-the-browser-and-press-enter-bb0aa2449c1a

A record
The A record is one of the most commonly used record types in any DNS system. An A record is actually an address record, which means it maps a fully qualified 
domain name (FQDN) to an IP address. For example, an A record is used to point a domain name, such as "google.com", to the IP address of Google's hosting server, 
"74.125.224.147".

This allows the end user to type in a human-readable domain, while the computer can continue working with numbers. The name in the A record is the host for your 
domain, and the domain name is automatically attached to your name. For example, if you want to make a record for www.yourdomain.com, you only need to enter 'www' 
for the name value in the textbox when editing the records for yourdomain.com.

CNAME record
Canonical name records, or CNAME records, are often called alias records because they map an alias to the canonical name. When a name server finds a CNAME record,
 it replaces the name with the canonical name and looks up the new name. This allows pointing multiple systems to one IP without assigning an A record to each host
 name. It means that if you decide to change your IP address, you will only have to change one A record.

CNAME records must be the only record on a zone, which is why they cannot be added to the apex of any zone as the apex is the place where the NS and SOA records for
 the whole zone must be placed. For this reason, we introduced the ALIAS record to give the same flexibility as a CNAME, but on zones where a CNAME would not other 
wise be permitted.

MX record
The MX record, which stands for "mail exchange", is used to identify mail servers to which mail should be delivered for a domain. MX entries must point to a domain,
 and never point directly to an IP address. If no MX record exists on a domain to which an SMTP server attempts to deliver mail, the server will attempt to deliver
 the mail to the matching A record.

In addition to the standard RDATA containing the location of mail servers, MX records also have a priority. The MX priority determines the order of mail servers to 
which mail delivery should be attempted. The mail server which has the lowest MX level should be the first target for delivery. For example, if you have MX records 
with levels 10, 20, and 30, servers should try to deliver the mail to the MX record with level of 10 and then to the others if delivery to the first fails.

NS record
An NS record identifies which DNS server is authoritative for a particular zone. The "NS" stands for "name server". NS records that do not exist on the apex of a 
domain are primarily used for splitting up the management of records on sub-domains.

The benefit of having multiple NS records on the apex zone is additional redundancy of DNS service. In order to get the most redundancy out of the NS records, they 
should be hosted on different network segments. If the NS records are not hosted on different network segments and the network goes down, your DNS will go down with
 it.

It is worth noting that the NS records set on a particular name server are different from the delegation for a domain set with the registry of the domain.

SOA record
The SOA or Start of Authority record for a domain stores information about the name of the server that supplies the data for the zone, the administrator of the zone 
and the current version of the data. It also provides information about the number of seconds a secondary name server should wait before checking for updates or before retrying a failed zone transfer.

TXT record
A TXT record allows domain administrators to insert any text into the DNS record. It is usually used to denote facts about the domain. A TXT entry was originally
 intended for human-readable text, but these records are dynamic and can be used for many purposes.

These records are not used to direct any traffic, but to provide information to outside sources. For example, TXT records are used by email systems to identify if an
 email is coming from a trusted source (via an SPF record). Another common use is "ownership verification". If you want to use a service like google webmaster tools, 
one method of verifying ownership is to add a TXT record to the domain with a randomly generated string. Google then checks for the record to have the proper value
 and confirms your control over the domain.
```
What is an SRV Record?
```
SRV (Service) records are custom DNS records. They are used to establish connections between a service and a hostname. When an application needs to find the location 
of a specific service, it will search for a related SRV record. If it finds one, it will sift through the list of services and their connecting hostnames to find the
 following:

Hostname
Ports
Priority and Weight 
IP Addresses, if relevant
Creating an SRV record can potentially save you time later on.

For example, a compatible new email client will pull your ports and settings preferences from the SRV record if you have one configured. Without the SRV record, a new email client will guess (usually incorrectly) these preferences.


The SRV Structure
This section will walk you through the different parts of the SRV record.


```

q) to change from old to new kernel for initial boot
```
check the gru2.cfg file 
awk -F\' '$1=="menuentry " {print $2}' /etc/grub2.cfg

grub2-set-default 3
grub2-mkconfig -o /boot/grub2/grub.cfg
shutdown -r now
```
q) how to recover grub failure?
```
https://www.youtube.com/watch?v=z047gbYCiWo&feature=youtu.be
Reinstalling the Boot Loader

when grub file is removed/damaged then system will not boot so and it ll go to 
grub console
grub>
	exit from grub console	#when u type exit it will take it to maintenance mode
	go to maintenance mode
	set boot from cd/dvd/usb
	then go to rescue centos filesystem> then it will open rescue mode
	then select option to rescue more (1)
	chroot /mtn/sysimage	#to change the console as root enviroment 	
	grub2-install /dev/sda
	grub2-mkconfig -o /boot/grub2/grub.cfg

Boot the system from an installation boot medium.
Type linux rescue at the installation boot prompt to enter the rescue environment.
Type chroot /mnt/sysimage to mount the root partition.
Type /sbin/grub-install bootpart to reinstall the GRUB boot loader, where bootpart is the boot partition (typically, /dev/sda).
Review the /boot/grub/grub.conf file, as additional entries may be needed for GRUB to control additional operating systems.
Reboot the system.


mount |grep -i ^dec
```
q)reseting root password
```
boot the system in rescuemode/recovery mode and 
go to shell
now the system will be read mode to enable it in write mode
mount -o rw,remount/
passwd
shutdown -r
```
q)inode
```
https://www.slashroot.in/inode-and-its-structure-linux#:~:text=Whenever%20a%20user%20or%20a,found%20from%20the%20inode%20table.
```

Q)Extending LVM?
```
1)check for free space in vg vgs and pvdisplay -m
2)lvdisplay to check lv details
)if u extend the lv from 2gb to 3g then u must also exted filesytem to 3g so that u can use entire 3gb lv
1)lvextend -L +1GB
2)resize2fs /dev/vg0/lv0

umount /<drive naem>/
mount -a # to check 
e2fsck -f /dev/vg0/lv0 # error checking
resize2fs /dev/vg0/lv0 1g
lvreduce /dev/vgo/lvo -L 1g

Q)how to reduce lvm
```
1 shutdown all app running onthe hosted lvm
2 take bckup
3 unmount lvm file system			
4 remove the entry from /etc/fstab
5 ext4
6 check for erros fsck
```
q) lvm snapshot
```
snapshot is pointing time copy , its pointing to blocks
snapshot will point to orginal data , suppose if data a1 in orginal data is deleted 
then this data will be avilable in snapshot but any data added after snaphot will not be protected
snapshot are there to protect data

creating snapshot
 lvcreate -L 1GB -s -n tecmint_datas_snap /dev/vg_tecmint_extra/tecmint_datas
lvextend -L +1G /dev/vg_tecmint_extra/tecmint_data_snap
Restore snapshot:
unmount /mnt/tecmint_datas/
lvconvert --merge /dev/vg_tecmint_extra/tecmint_data_snap
```
q) to restore deleted lvm?
```
vgcfgrestore --list VG
checkt the deleted vg file and run the following
vgcfgrestore -f /etc/lvm/archive/<vg.000.vg> VG
mount -t ext4 <lv> <nmame>
```
q) to check filesystem:
```
lsblk
file
fdisk

```
q) scaning for new luns
```
echo "- - -" > /sys/class/scsi_host/host2/scan
The three dash ("-  -  -") of the command act as wildcards meaning rescan everything. Remember that the three values normally stand for channel, SCSI target ID, and LUN.
q) migrate lvm from one server to another server
umount /data01
vgchange -an data_vg  #vgchange -- volume group "data_vg" successfully deactivated
vgexport data_vg      #vgexport -- volume group "data_vg" successfully exported #It is now necessary to export the volume group. This prevents it from being accessed on the ``old'' host system and prepares it to be removed.
remvoe disk from server and connect it to new server
pvscan
vgimport data_vg			importin on lvm2
vgimport data_vg /dev/sdb1 /dev/sdb2        #importin on lvm
vgchange -ay data_vg
mkdir -p /data01
mount /dev/data_vg/lv_data01 /data01

```
q) scaning new device attached to linux machine
```
attach device like cdrom
then identify the name by running dmesg|grep dvd
```

Q)explain entries of /etc/fstab?
```
/dev/mapper/rhel-root       /	        xfs	     defaults	     0 0
<   dev/devicename  >  < MountPoint >  <file system> <mount options>
0= zero means exclude from backup non zero dump program enable device to backup
0= fsck check, if zero excluded to check fsck, non zero value 2 partiation will be checked

```
q) u cannot create filessytem more than 2.5tb using fdisk as its based on MBR
```
to create file ssytem size above 3tb u have to use gpt(GUID)
convert above 3tb file to GPT
	1) parted /dev/mapper/disk
	2)print
	2)rm 1
	3)mklabel gpt
	4) pring
	5)mkpart primary 1GB 6.TB	
	6)q
	7) mkfs.ext4 /dev/mapper/disk
	8) mount
```

q) restricting the user to particulr service can be done on visudo file
``````
user ALL=(ALL) NOPASSWD: /bin/ftp/, /bin/telnet, /bin/ssh

Q)what is suid?
```
suid is file permission, which allows other user access the owner file 
eg: /etc/passwd is file which is created by root and other user can access it as root permision

```
Q)what is setuid setgid stickbit
```
Setuid bit flag can provide regular users the ability  to run the same access as the owner of the executable 
file. It is represented by an s in the owner's permission
class.
chmod u-s /usr/bin/su to remove 

Setgid: Setgid bit is set on executable files at the group  level. Setgid bit flag 
can provide regular users the ability to run the same access as the group members of  the executable file. 
chmod g-s /usr/bin/wall


Sticky bit is set on public writeable directories to prevent moving or deletion by regular users.
chmod o+t /tmp or chmod +t /dir

```
Q)how to provide access to single file to multiple users and groups with custom permission??
```
ans: using acls we can do this 
	getfacl
	setfacl
```	
q) lsof: is used to check which file is open
```
when ever  ./ mount file fully utilized to 99% and u dint find any file to delete then u can delete tmp files

lsof |grep deleted
lsof|grep deleted | grep ".tmp" | awk '{print $2}'| xargs kill -9
lsof|grep deleted | grep ".tmp" | awk '{print $9}'| xargs rm -f
```
q) umask value is present in : /etc/profile : this is default file permisson
	
q) recovering file from ext4
```
	sudo extundelete /dev/sdb1 -restore-file home/angelo/other.txt
	extundelete /dev/sda6 -restore-all
```


q)iscsi linux target and initiator configuration
```
iscsi(intetnet small computer system interface),its a internet based storage networking standard
for linking data storage facilites it provides block level access to storage
device by carring scsi commands

iscis will have have target server and client system, where target sever provides its storage to client over interntes
and client server can attache the storage and by pvcreate vgcreate lvcreate mkfs mount

server ip(target)
clinet ip(target)
target server : target.service
port number: 3260
inintiator service: iscisd.service

1) attache drive to target system
2) create lun using fdisk utility
	fdisk /dev/sdb
		n # new partition
		p # primary
		default use disk based on req, full size  
 		select partion as lvm code is "8e"
		wq
	partprobe /dev/sdb	#to update the sdb table
	pvcreate /dev/sdb1
	vgcreate vg0 /dev/sdb1
	lvcreate -l 100%FREE -n lv_vg0 vg0
	lvs
now donot formrot the drive
yum install targetcli	#this tool helps to convert disk to iscsi luns
	targetcli
	create backstores
	/backstore/block create LUN /dev/vg0/lv0
	/iscis create iqn.server1.node1:disk1
	/iscsi/iqn.server1.node1:disk1/tpg1/acls create iqn.server1.node1:disk1  #create network acsl to allow access
	/iscis/iqn.server1.node1:disk1/tpg1/luns create /backstore/block/LUN #create lun and map to clinet ip
	/iscis/iqn.server1.node1:disk1/tpf1/portals	create <client ip> #create portal and maek it asscisble by client
	if u get error during portal create then delete existing portal
	/issci/iqn.server1.node1:disk1/tpg1/portals delete 0.0.0.0 ip_port=3260 	
	/iscis/iqn.server1.node1:disk1/tpf1/portals	create <client ip> #creat
	save
firewall --cmd --permanent -add-port=3260/tcp
systemctl restart target.service

client side
yum install iscsi*	
systemctl start iscsid 
vi /etc/iscsi/initiatorname.iscis
	add the initiarot name in this file
iscisadm -m discovery -t st -p 10.200.20.250
iscisadm -m node -T iqn.server1.node1:disk1 -p 10.200.20.250 -l # to login to target
fdisk -l
```


q) nfs installation
```
yum install nfs-utils
mkdir /var/nfsshare
chmod -R 755 /var/nfsshare
chown nfsnobody:nfsnobody /var/nfsshare
nano /etc/exports
	/var/nfsshare    192.168.0.101(rw,sync,no_root_squash,no_all_squash)
	/home            192.168.0.101(rw,sync,no_root_squash,no_all_squash)
systemctl restart nfs-server

client side
yum install nfs-utils
mkdir -p /mnt/nfs/home
mkdir -p /mnt/nfs/var/nfsshare
mount -t nfs 192.168.0.100:/home /mnt/nfs/home/
```
Q:1 Why to use NFS ?
```
Ans: A Network File System (NFS) allows remote machine to mount file systems over a 
network and interact with those file systems as though they are mounted locally. This enables system administrators to consolidate resources onto centralized servers over the network.

Q:2 What is the default port of NFS server ?
By default NFS uses 2049 TCP port.

Q) What are configuration files of NFS server ?
‘/etc/exports’ is the main configuration file that controls which file systems are exported to remote hosts and specifies options.
‘/etc/sysconfig/nfs‘ is the file through which we can fix ports for RQUOTAD_PORT, MOUNTD_PORT, LOCKD_TCPPORT, LOCKD_UDPPORT and STATD_PORT
ro: The directory is shared read only; the client machine will not be able to write to it. This is the default.
rw: The client machine will have read and write access to the directory.
root_squash: By default, any file request made by user root on the client machine is treated as if it is made by user nobody on the server. (Exactly which UID the request is mapped to depends on the UID of user “nobody” on the server, not the client.)
no_root_squash : if this option is used , then root on the client machine will have the same level of access to the files on the system as root on the server. This can have serious security implications, although it may be necessary if you want to perform any administrative work on the client machine that involves the exported directories. You should not specify this option without a good reason.
no_subtree_check : If only part of a volume is exported, a routine called subtree checking verifies that a file that is requested from the client is in the appropriate part of the volume. If the entire volume is exported, disabling this check will speed up transfers.
sync : Replies to the NFS request only after all data has been written to disk. This is much safer than async, and is the default in all nfs-utils versions after 1.0.0.
async : Replies to requests before the data is written to disk. This improves performance, but results in lost data if the server goes down.
no_wdelay : NFS has an optimization algorithm that delays disk writes if NFS deduces a likelihood of a related write request soon arriving. This saves disk writes and can speed performance
wdelay : Negation of no_wdelay , this is default
nohide : Normally, if a server exports two filesystems one of which is mounted on the other, then the client will have to mount both filesystems explicitly to get access to them. If it just mounts the parent, it will see an empty directory at the place where the other filesystem is mounted. That filesystem is “hidden”. Setting the nohide option on a filesystem causes it not to be hidden, and an appropriately authorised client will be able to move from the parent to that filesystem without noticing the change.
hide : Negation of nohide This is the default

Q:6 How to list available nfs share on local machine & remote machine ?
showmount -e localhost
Q:9 How to check iostat of nfs mount points ?:
nfsiostat
Q:12 How to reexport all the directories of ‘/etc/exports’ file ?
Ans: Using the command ‘ exportfs -r ‘ , we can reexport or refresh entries of ‘/etc/exports’ file without restarting nfs service
```



q)firewall working
```
yum install firewalld
/etc/firewalld/firewalld.conf
firewald-cmd --state
firewall-cmd --get-zones 
firewall-cmd --get-services
firewall-cmd --get-default
firewall-cmd --permenant --add-port=3306/port # add it as port
firewall-cmd --permenant --add-port={3306/port,80/port,8080/port} # add it as po
firewall-cmd --permenant --add-service=mysql
firewall-cmd --permenant --add-service={ldap,mysql}
netstat -nltp to chec port status
#port fordwardin
firewall-cmd --add-forword-port=port=8080:proto:tcp:toport=80      # anything comming to port 8080 redirect it port80
firewall-cmd reload
firewall-cmd --permanent --add-rich-rule 'rule family=ipv4 source address=192.268.10.200/24 forward-port port=153 protocol=tcp to-port=123'

```
q)NIC Bonding
```
# nmcli dev status
enp0s8
enp0s9
4- Load bonding driver in Kernel:
# modprobe bonding
5- Verify:
# modinfo bonding
6- Add logical Interface "bond0" with load balancing
policy "round-robin", IP 192.168.1.120/24 and
gateway 192.168.1.1: 
# nmcli con add type bond con-name bond0 ifname bond0
mode balance-rr \ip4 192.168.1.120/24 gw4 192.168.1.1
Check file:
#  cat /etc/sysconfig/network-scripts/ifcfg-bond0
- Add two added interfaces as slaves:
Add 1st Interface enp0s8
# nmcli con add type bond-slave ifname enp0s8 master
bond0
Add 2nd Interface
# nmcli con add type bond-slave ifname enp0s9 master
bond0
Check Files: 
# cat 
/etc/sysconfig/network-scripts/ifcfg-bond-slave-enp0s8
and 
/etc/sysconfig/network-scripts/ifcfg-bond-slave-enp0s9
- Activate bond0
# nmcli con up bond0
-  Show connection info for bond and slaves:
# nmcli con show | egrep 'bond0|enp0s8|enp0s9'
# reboot

```
q)upgrading kernel version
```
uname -r
check /boot dirctory , it should not contain more than 500
download kernal form url
yum --enalberepo=elrepo-kernel list all|grep kernel
yum --enablerepo=elrepo-kernel install kernel-ml
reboot
```
q)systemctl
```
systemctl list-dependencien httpd
systemctl list-unit-files
systemctl set-default multiuser.target
systemctl mask http,firewalld
systemctl unmask httpd,firewalld

```


q)selinux
```
getenforce
sestatus
setenforce 0 # allows everytihn it logs

chcon #to change security context

security enanched linux
why u need selinux:
selinux provides diffrent level of securitys
1 port level
2 service level
3 file level

eg: if port 80 is allowed and port trys to access other service which is not designated to port 80 then 
selinux will block this

selinux modes
1)enforcing - Enabled
2)permissive - Not Disabled
3)disabled - off

/etc/selinux/config

ls -lz will show u context

```

q)syslogs
```
in linux /etc/rsyslog.conf # tell where to store the logs
all logs are stored in /var/log

```

q) to add rpm repo from cd
```
mount cd/dvd to dirctory
cp the content to locol repo
create dir /etc/yum.repo.d/<repo file>

repofile:
[reponame]
name= <userdfined name>
baseurl=file:///mnt
enable=1
gpgchekc=1
gpgkey=gile:///mnt/rpm.key


```
```
q) Adding ssl certificate to httpd
yum install mod_ssl
firewalld -cmd --permenant --add-service=http
firewalld -cmd --permenant --add-service=https
setenfore 0
create csr key and crt
and copy to safe location
then edit /etc/httpd/conf.d/ssl.cof
<virualHost> *:443>
change server name
enable ssl ciphersure,sslhonotsipher order on,sslcertificatefile ,key file





ssh
--------------------------
ssh config path /etc/ssh/sshd_config  and to change port update the same in this file
to connect ssh diffrent port from putty use ssh -p 2048
ssh supports symmetric and asymmetric encription method
to disable root login update sshd_config file "permitrootlog no"
enable only key based login: set rsaauthentication and pubkeyauthentication to yes and 
telnet sends data as plain text
limiting ssh access to specfic subnet: this will increase secure e
edit sshd_config file and update "AddressFamily <subnet>"
ssh cipher types: 3des, blowfish, des 
debuggin ssh : use "ssh -v"
ssh version check: "ssh -V"
ssh for ipv6: ssh -6 user@hostname
ssh to load log to specfid file: ssh -E log_file
ssh idle timeout: edit sshd_config file "ClinetLiveInterval 15m"
"ClientAliveCountMax 5"
------------------------------------------------------



q) what is zombie process
its process that has completed execution but still has entry in process table


q) diffrence bw locate and find

find searches in the real system. Is slower but always up-to-date and 
has more options (size, modification time,...)

locate uses a previously built database (command updatedb). 
Is much faster, but uses an 'older' database and searches only names or parts of them.

q)how to patch the server

download patch manager software
open software
click on retry angent 
and download linux agent 
and copy the agent in linux machin


q) nmtui


Q)Password Complexity Policy On CentOS 7

/etc/security/pwquality.conf or /etc/pam.d/system-auth configuration file is used.





sed
sed -e 's/input/output/' my_file 
sed -e 's/input/output/g' my_file 
sed -e 's/input/output/' my_file > new_file
sed -i -e 's/input/output/' my_file 
sed -e 's/\/bin/\/usr\/local\/bin/' my_script > new_script			#special symbol, like '/'(e.g. in a filename) or '*' etc? Then you must escape the symbol
sed -e 's/[0-9]*/(&)/' my_file						# wildcard as part of your search
where [0-9] is a regexp range for all single digit numbers, and the '*' is a repeat count, means any
number of digits.
sed -e '/^#/ d' my_file							#if you wanted to delete all lines that start with the comment symbol '#' you could use














Vm ware software defined data center platform
its as software defined data center platform
VMware Cloud Foundation makes it easy to deploy and run a hybrid cloud.
 VMware Cloud Foundation provides integrated cloud infrastructure 
(compute, storage, networking, and security) and cloud management services to run enterprise applications in both private and public environments.
Vsphere
vsan
nsx 




Interview qs1
##########################################################################
##SSHD
ssh default port is 22

/etc/ssh/sshd_config   #ssh master config file
#when u first login to shell u will be in login shell but when u switch user u will be in intreactive shell not be in login shell
i  

first login(login shell)      --------->.bashrc_proile  will be executed
switch user(interactive shell)--------->.bashrc 	will be executed

#insted of login to intractive shell logging in to "login shell" and 
to use all bash_profile use any one of this 
su -
su -l 
su --login

/etc/profile		#its a global configuration file
#############################
#############################################
Archive
stat /directory #will display the directory details
du -sh /  #to list size of all directorys
du -ah #
du -cbha # 
fdisk -l /dev/sda
df -ih #to display inodes
df -t xfs #(-t)filter type
#######################
patching servers
1)critical update
2)security updates
3)bug fixes
4)enanchments
5)os updates
########################3
swap memory and creating

actual memory is 32gb if u open many application which exceeds 32 gb then 
we can use swap space:
kernel identifys the inactive application and movies that into swap space which is on hdd

################################

###################################3
groupadd finance
getent group	#todisplay all group details
directory needs execute permission to open 
cp command doses not preserve acl rules
mv command preserve acl rules
chmod ug+X		#this command will give execute permission only to directorys not all files
chmod ug+x	#this command will grant execute permission for both files and folders

#####################################
/dev/null :
is a space where wat ever u sent it will be cleared
eg:- 

pipe command accepts standard output not error
asdfasdf 2>&1 | grep 'command'
adfadsf 2> |grep 'command'		#error
##########################################################################
## Redirecting standard error and output to file

asdfasdf 2>> log.txt
asdfasdf
cat log.txt
pwd 2>> log.txt
cat log.txt
pwd >> log.txt 2>&1
cat log.txt
catf log.txt
pwfd >> log.txt 2>&1
###############################################################################################
## reboot/shutdown/boot

/usr/lib/systemd/system		#where all systme target files are located here, system will first check this dir
/etc/systemd/system    		#its additional config file like apache,custom config fiel
we will have default.target symlink in thid dir so wen ever this target is changed this symlink is updated

shutdown -r +5	will reboot in 5min	#number of miniutes t wait before reboot this will send wall message
shutdown -c 		#to cancel reboot
w		# to check who is login
shutdown -r 00:00		#schedulet to reboot at nite 12 oclk
systemctl halt/halt/shutdown -h /shutdown -h now  #shutdown command

## boot system in diffrent targets manually

init # will allows to start one service at a time
systemd will allows to start multiple service at a time

systemctl -t ### to check diffrent type of unit config files
systemctl list-units --type=target
systemctl list-dependencies multi-user.target		#to list dependencies of multi user targets
when ever system enters in multi user target then all the service will be called
systemctl get-default  # will reture default targets
systemctl list-dependencies graphical.target|grep multi.user # this shows wen ever we are 
in graphical target then we need all targets which are in multi.user.target

#this are four targets that generaly we use 
multi.user.target
graphical.target
emergency.target
rescue.target		#this will be run in read only mode,in sigle user mode

systemctl isolate <target name>	#to move from one target to another we must use systemctl isolate
systemctl set-default <target name>

## To intrupt the boot process and specfiy to go into diffrent targets
reboot
when boot menu asks to load kernel 
press "e"  # to edit the selected item , u can c grub config
search kernel like"linux16 /vmlinuz" and add this at end of line
systemd.unit=rescue.target
eg:systemd.unit=<target>
###############################################################################################################
## to change root password
grug allows us to select the kernel in that kernel needs to be loaded some where but i
initaly there will be no disk, so kernel allows to load local kernel that kernel inside memory
and that kernel has version of systemd/root device, it mounts feature devics as /sysroot on initramfs
this memory section is called initrmfs as soon as initilization is over then it hands over control
to local disk and pid of 1 in systemd

so to reset root password, we shold to get into initramfs debug shell which is basical working
in memory

step1
find kernel "linux16/vmlinz" and append the "rd.break" at end
this will take us into initrmfs debug shell
step2:
initialy sysroot will be in read only and u cannot use passwd cmd so you have to mount the directory as rw
mount -oremount,rw /sysroot
cd sysroot	# navigate into sysroot directory
cd etc
in order to mount sysroot directory ar root director use chroot
chroot /sysroot    #now it gives access to passwd command
passwd
 step3
by default we are using selinux when we modifie passwd context of selinux will be changed so we have to relable the file, 
once passwd is changed we have to relabel all as selinux , so in order to system to instructed to 
relable we just have to make sure file exist inside the root dir,its hidden files
touch /.autorelabel

if u dont do this then password change will not be successful

step4:
exit
exit

# adjust process priority and kill process 
ps 
ps -aux
pgrep 	#combaind ps command and grep command eg: pgrep gnome
pgrep httpd -l  #to list names 
pgrep -u <user> -l # display all process running by users
pgrep -v -u <juser> -l # -v means inverse, which are not user it will list that process

## pkill command

pkill httpd # it greps for all procesee in the name httpd and kills it
kill -l
kill -15 / kill SIGTERM # kill command default will be sigterm (15)
kill -1 {is equal to SIGHUP: 
SIGINT: Keyboard intrrupt
SIGQUIT: request the process to quit
SIGKILL: anythin it will kill the process
SIGTERM: clearnup and terminate the signal
SIGSTOP:
suppose if u want to stop the process not to terminate then u can use SIGSTOP
kill -SIGSTOP %5
SIGCONT:
if u want to continue the stoped process then u cant user SIGCONT

## PS

ps aux
ps -u <user>

## setting nice and renice
u can set the priority for the process using nice priority is from(-20 to 19), lower the level higher the priority
dd if=/dev/zero of=/root/test.file bs=1M count=1024	#to create gigbyte file

nice -n 0 httpd   #starts process with specfied nice value
renice -n 1 $(pgrep httpd)  # updates running process nice value

##Top Command

load average   			#it determins % of load average
in order to find total load usage first find total number of cpus(cat /proc/cpuinfo)
uptime cpu/number of processor
eg: 2.5/2 = 1.25 #which means process is using 125% of cpu 

## rnice in top command
top
press "r" and enter the nice value

## top command fields
RES: non swap physical memory using
SHR: amount of shared memory avilable to task, which means this task will sharign memory with other tasks
shift+<p> or shift+<m> #to sort by
##to kill process from top
press k 
and enter the pid

top -d 2 ## to set top command interval


## inorder to kill the user ps use
pkill -u thiru sshd

now to reset root passwd we will break kernel and will make use of


# Log Files
/var/log 
## journactl
journalctl sends log to /var/log , 
journalctl			#logs all kernal logs,journald is not persistant
this ll dump the all info in the journal deamon
/run/log/journal		# journal info are stored in this loc

#making journald as persistant

/etc/systemd/journald.conf  # change storage=persistent
journalctl -n		    #last 10 lines
journalctl -xn		    # "x" provides addtional texts
journalctl _SYSTEM_UNIT=httpd.service  #to display system unit config files systemctl -t help
journalctl 
## rsyslog

## systemd-analyze		#how fast system booted up
systemd-analyze blame		# it will how long each process took


# MBR & GPT
MBR:32bit,4primary partitaon,each 2tb
mbr was developed on 1982, mbr can have only 4 primary partitons, each primary can be only and one extended partiation
2tb in size
FDISK:
its tool which used for MBR based device
fdisk /dev/sdb > select n(new) > p(primary) >default>default 2048> +500M >t>partiation type(8e) > w >
begning of record is 4mb which maintenance disk info, so it starts from 2048

## in order to use disk u have format is using mkfs
mkfs ext4 /dev/sdb1

blkid 		#will display the block storage uuid
partprobe	#it reload the partiation info

blkid 
best practice is to mount using uuid insted of device name


GPT: 64bit,128 primary device,8zb bytes
GPT based partation runs on uefi defice, 
GDISK:
its tool which is used for GPT based disks
gdisk /dev/xvdf > select n(new) > p (primary)>default 2048> +500M>filesystem default is linux filesystem(8300) > w >
mkfs -t xfs /dev/xvdf1
mount /dev/svdf1 /mnt/mymount 	

# delete  partation
gdisk /dev/xvdf > d>w>

#LVM
inorder to use physical volume, physical volume must be initilized as lvm(label)
by doing this labels place on first part of volume helps to identify the metadata about physical volume to lvm,
its is placed in second 512 bytes on physical volume, u can have either zero one or two copies of meta data
stored on each physical volume, by default one copy is stored on physical volume, once number of copies is configured
u cannot changed,
fisrt copy is stored at start of device & second copy is stored at end of device

#vg ,we have physical volumes,volume group,lvm
extends are inside volumegroup,extends is smallest unit that can be assigned to vg, 
vg extends are reffred as physical extents(PE) and lvm is allocated in two sets of logical extents 

we can define logical volume based on number of PE, if u want create lvm using nubmer of PE
then u have to mention it using "-l" in lvcreate eg: lvcreate mydisk /dev/sdb -l 2 where 2 is number of PE so 4m*2=8mb lvm

step1: create partiation using gdisk>lvm>w
step2: pvcreate <partiation>
step3: vgcreate mydisk /dev/sdb -L 100M
step4: lvcreate -n mydisk_lvm -L 100M
setp5: mkfs -t ext4 /dev/vg/lv
step6: mount /dev/vg/lv /mnt/dir
lvremove /dev/vg/lv
vgremove /dev/vg
pvremove /dev/sdb

xfs: can only be increased not desresed
ext3: can be increased and decresed 
# configure system to mount filessystem at boot by uuid or label

step1: create 2 partation
setp2: mount xfs and ext4 file system
step3: 
	a)xfs_adm -L <label name>  /dev/xvdf1	#create label for xfs file system
	  xfs_adm -l /dev/xdv1	#prints the label

	b) tune2fs -L <lable name> /dev/xvdf2	#create label fro ext4 filesystem
		tune2fs -l <lable name> /dev/svdf2 #print the filesystem label	

to mount use UUID from blkid and update it on /etc/fstab

stet5: fstab/
	UUID=<UUID> 		/ 	xfs	defaults	1 1
	LABEL=<label name>	/	ext4	defaults	1 2
mount -a

# creating swap space
step1: fdisk /dev/sda > p >lvm>w
step2: pvcreate /dev/sda1
step3: vgcreate swap_vg /dev/sda1
step4: lvcreate -n swap -L 2G /dev/sda1/swap_vg
step5: mkswap /dev/swap_vg/swap 
step6: swapon /dev/swap_vg/swap
step7: use the UUID and mount it on fstab 
fstab:
	UUID=<>		swap	0 0 
swapon -a	# to enable all swap 
swapoff -a 	# to turn off all swap
swapon -s	# which partation has swap space

# Mount UnMount and use vfat ext4 xfs
vfat: allows windows user to access the file system

mkfs .vfat /dev/sdb
mkdir vfat
mount /dev/sdb /mnt/vfat
df -h
attach it to /etc/fstab

## ex4	supports 16tb filesystem of 50tb
mksf.ext4  /dev/xdvf1

fsck.vfat
fsck.ext4 /dev/xdf1	#to check filesystem
fsck: 
fsck cannot be run on mounted file system
dumpe2fs /dev/sdb	#this will give u all filesystem  details also provide number of inodes avilable
mkfs.xfs   #this filesystem provides high throughput and 500tb of storages
XFS • Known for parallel processing and high I/O throughput; journaled file system that supports
up to 500TB file size on Red Hat 7 with 500TB in file system size
» mkfs.xfs /dev/xvdf1 • Create XFS file system on device
» mount /dev/xvdf1 /mnt/location • Mount file system at location
» xfs_repair /dev/xvdf1 • Check for file system consistency
» xfs_info /dev/xvdf1 • Get details of file system
» xfs_admin /L labelname /dev/xdf1 • Label the device


xfs_info	#this provides info about xfs disk
xfs_repair	#repair any issue on partation

# Mount & Unmoun CIFS and nfs

CIFS: it allows us to share from windows machine to linux/unix machine
sama it tool which allows us to use cifs
CIFS Using Samba
 yum install sambaclient cifs-utils nfs-utils

# sama share > mount -t cifs -o username=smbusername,password=smbpassword //serverip/share_name /mnt/mountlocation
#nfs share   > mount -t nfs -o username=smbusername,password=smbpassword /serverip/share_name /mnt/mountlocation

/etc/fstab persistent configuration:
***/etc/fstab file
//serverip/share_name /mnt/mountlocation cifs username=smbusername,password=smbpassword 0 0
***
NFS
yum install -y nfs-utils
mount -t nfs serverip:/mountlocation /mnt/mountlocation
/etc/fstab persistent configuration:
serverip:/mountlocation /mnt/mountlocation nfs defaults 0 0

# extending lvm and attaching gpt partation and moving content to gpt without distruption

step1: fdisk /dev/sdb > p >default>default> lvm>+1G>W>
step2: pvcreate /dev/sdb1 |pvs
step3: vgcreate sdb1_vg /dev/sdb1 -L 500M
step4: lvcreate -N  lv1_sdb1 /dev/sdb1_vg/ -L 500M
step5: mkfs.ext4 /dev/sdb1_vg/lv1_Sdb1
step6: mount /dev/sdb1_vg/lv1_Sdb1 /mnt/dir
cd /mnt/dir
touch f1.txt f2.txt

## to change mbr partiation to gpt partation and dont want to intrupt the actual data

step1: gdisk /dev/sdc > n>default>default>size>linux lvm>w>
step2: pvcreate /dev/sdc1
step3: vgextend /dev/vg_sdb1 /dev/sdc1 
step4: pvmove /dev/sdb1 		#will copy the old volume to new volume in same group
step5: vgreduce /dev/vg_sdb1 

## extentd lvm

lvextend -L 5G /dev/vg_sdb1/lv_sdb1
resize2fs #for mbr based partation
xfs_growfs /mnt/dir	#gpt based partation

##ACL
+ sign will indicates that file has ACL
getfacl

setfacl -m -R u:thiru:rw file1		set acls for user & -R for recursively
setfacl -m g:thiru:rw file1		set acls for group
setfacl -m u:thiru:-rw file1

getfacl file1 #
by default mask in acl will have permission of user set
setfacl -m m::r file1 #to set mask for file1 to read permission
setfacl -m m::- file to remove mask
chmod will updates mask


#default acls 
wen ever files are created with in the directory then files will inheriate the default acls
setfacl -d -m u:thiru:rw dir1 #setting default acl to files not directory 
the default dosent apply to directory now if u cd to dir1 u ll get error
getfacl dir1
setfacl -x u:thiru dir1 # to remvoe acls
setfacl -x -d u:thiru dir1 # to remvoe default acls



# Networking in linux

ip #ip command
ip addr show etho0	#
ping -c5 
traceroute
tracepath 
netstat
ss -a		# new version of netstat
ss -at	#all tcp connection
ss -atn #with port number

ip -s link show eth0

#network manager

sudo ipconfig	#to config ip address
sudo dhclient	#to get ned ip from dhcp server
sudo systemctl restart network
sudo /et
ls /sys/class/net	#this will have network details

##NMCLI
nmcli (double tap it will show avilable options)
	agent       device      help        networking
	connection  general     monitor     radio
nmcli connection
nmcli agent
nmcli device
nmcli networking
nmcli general
nmcli monitor
ncmli /dev/status
ncmli con show
ncmli device show ens33
nmcli con down  

##network manager hostname
by default system will look for entry in host file, and then dns server if u want to change
then update the order in the /etc/nsswitch.conf file
**
hosts: files dns myhostname
**

search mydomain.com	#is keyword added in resolve.conf file so that it will append the mydomian.com to the entry
srv.mydomain.com	#without search
srv			#with search	
getent hosts google.com	#this will return google.com host name

#Scheduling AT and Cron
## At
at
atrm 1 #to remove the jobs using job name
atq	#to display the jobs
at.deny   #if user is specfied in this file the user is not allowed u to use at command
at.allow  #all user execpt the user specfied in the file do not have permission to execute at command
if at.allow file exist then the user which is specfied in this file is only allowed to use at commands
journalctl -xn # to c job executed status 

## Cron job

crontab utility that allows us to edit users cron , regular user can schedul ther crons
however system cron is configure in /etc/cron. 
we donot use crontab file in /etc/crontab in new rhel

annacron #is utility that allows us to run the job which is not run(missied oppturinity) for defined days


# starting and stoping of service

systemctl status httpd
systemctl start httpd
systemctl enable httpd
systemctl restart httpd
systemclt is-enabled httpd
systemctl unit-files
systemctl get-defaults

#configure system to boot into specfic targets

#kickstart server

kickstart.cfg
yum install system-config-kickstart 	#this will start gui based kickstart config tool

#system date and time

timedatectl		#gives info about date time
timedatectl set-ntp true/false
timedatectl list-timezone
tzselect 	#to search for timezone
timedatectl set-timezone asia/kolkata
timedatectl set-time 12:30 PM

#Ntp
yum install chrony
chronyd			#ntp deamon
chronyc sources -v 	#to get list of servers that communicate to get time
ms | name/ip | startum  | poll | reach | lastrx | last | sample |

startum: number of hops it takes to reach server
chronyc tracking

/etc/chrony.conf # chrony setting file be located here


#rpm ,yum
insted of updating all packages , check package need to be update and update the same 
yum list installed
yum provides /var/www	#to check which package created this directory
yum repolist all
yum-config-manager --add-repo=<repo>
yum-cionfig-manager --disable jenkins
yum-config-managet --enable jenkins


## rpm  #it installs 
rpm -qa 		# to query the package
rpm -ivh		# i for install, v for verbose h to show progress bar
rpm -e 			# to remove package

## local repo , how to use dvd iso rpo

setp1: mount -o loop rhel-server-7.1.x86_64-dvd.iso /repos/local  #mount the dvd iso 
step2: 			#extract from dvd
step3: create local-repo
[local-repo]
name=red hat linux local repo
baseurl=file:///repo/local
enable=1
gpgcheck=0

### gpgkey is importat so that u can verfiy the repo is valid repo


# update the kernal package

uname -r
yum install kernal 
yum clean
yum list kernal		# showl liist of installed and update kernal 

installing kernal using rpm
yumdownloader kernel
yum install linux-firmware
rpm -ivh kernal


# changing diffrent kernel, modifiy the bootloader to point to diffrent kernel 	

step1:yum list kernel	#check for list of kernel avilable	
step2: grug2-set-default 0 or 1 or 3 #by default 0 is most recent version 

# create delete and modifiy the usesr

id
root user has id=0
useradd thiru 
usermod -U thiru
usermod -u <user-id> thiru #to change user id
useradd -u 1050 -d /home/thiru
userdel -r or -f
/etc/default/userdd		#this file consist of default value for user like(group,home,inactive,expire,shell,skel,create_mail_spool)

usermod -s /sbin/nologin  thiru #changing user to nologin
usermod -e 			#wexperiation date
chage -l <user>		#will display the passwd details 
chage -E		#EXPERATION

## creating goup
groupadd # to create new group
getent group #list all groups in the system
cat /etc/gshadow	#to view group details
getent group thiru	#it returns all of the group the user belongs to
groups <users>		#displays primary and supplimentry group
usermod -g <primary grou> <user> # this will change primary group of user
groupmod -n		#to change the group name etc
groupmod -g		#to chage group id
groupdel <group>	#deleteing group u cannot the delete the group which is primary to another user

# Set Gid / SGID

when ever user create a file in group directory then if file has his own permission then
other will not be able to access it so, in order to over come this we use sgbit
when sbit is set file inherites the parrent directory permission 

dhmod g+s <directory>
#configure system to use existing authentication
connecitng for single sign on	

# connecting ad to linux

yum install realmd 

#firewall 
yum install firewalld firewall-config
systemctl start firewalld
systemctl enable firewalld

firewalld has two type 
1)runtime changes: changes made at this level(run level change) will not be
 persistant
2) to make persistant use --permanent and the --reload firewall

firewall-cmd
firewall always groups inside a zone,each zone can be configured 
firewall-cmd --get-zones
firewall-cmd --zone=public --permanent --add-port=80/tcp
firewall-cmd --reload
firewall-cmd --list-all
firewall-cmd --set-default-zone=internal
firewall-cmd --get-default-zone
firewall-cmd --list-all-zones
firewall-cmd --set-default-zone=internal
firewall-cmd --get-default-zone
firewall-cmd --get-zone-of-interface=enp0s3  #To check zone in which interface is bounded

Services are set of rules with ports and options which is used by Firewalld. 
Services which are enabled, will be automatically loaded when the Firewalld service 
up and running. By default, many services are available, to get the list of all 
available services, use the following command.

cd /usr/lib/firewalld/services/		# To get the list of all the default available services,

firewall-cmd --get-service
firewall-cmd --add-service=rtmp
firewall-cmd --zone=public --remove-service=rtmp
firewall-cmd --add-service=rtmp --permanent
firewall-cmd --reload
firewall-cmd --permanent --add-source=192.168.0.0/24
firewall-cmd --permanent --add-port=1935/tcp
firewall-cmd --reload 
firewall-cmd --list-all

Adding Rich Rules for Network Range

firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="http" accept' 
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="http" accept' --permanent

 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="https" accept'
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="https" accept' --permanent

 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="vnc-server" accept'
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="vnc-server" accept' --permanent

 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="postgresql" accept'
 firewall-cmd --add-rich-rule 'rule family="ipv4" source address="192.168.0.0/24" service name="postgresql" accept' --permanent


# selinux
getenforce
setenforce
cd /etc/selinux
ls -Z			#will display context
use Z to display the selinux context
pa auxZ
restorecon index1.php		#use this it resotre the context on the file/folder

by default wen u configure selinux all file system are labeld, if u want to force a relable file/directory u need to make 
sure the .autorelable is present in root directory
semanage fcontext -l	#waht context 
chon #to set context manually
semanage fcontext -a httpd_sys_conten_t '/content(/.*)?'		#-a means add , -t for type type context,




##LOG ROTATE
logrotate is designed to easy admin of systems that generate large number of log files.
normaly logrotate is run as cronjob that is daily /etc/cron.daily
logrotate can done based on follwoing criteria
1)based on log file size
2)time base log rotation
3)compress old log files
4)clean log files which are matching log rotation rule
5)create new files after log rotate


cat /etc/cron.daily/logrotate		#logrotate script
/etc/logrotate.d			#logrotate file will be in this loctaion

if u want create a custom logrotate script then u can create script and place it in /etc/logrotate.d
**
/tmp/log/*.log{
	create 0644 root	#set owner permission
	daily			#Running daily
	missingok		#if no log file then dont rise ny error
	rotate 4		#keep 4 log files
	compress		#compress log file
	notifempty		#if log file is empty then dont rise erro
	postrotate		#after rote run this script
		/scripts/backuplog.sh	
	endscript
}

to execute created file 
logrotate -f /etc/lograte.conf



##epel repositary

##recovery deleted files on linux
testdisk #is free datarecovery software 
VI

press following in command mode
#d to delete the line
#y copy the line	
# shift+g		#to navigate to top
# shift+G		#to navigate to bottom
# cc will remove the line and will go to insert mode

Swap Memory
q)understanding swap memory

Swap is a space on a disk that is used when the amount of physical RAM memory is full. When a Linux system runs out of RAM, inactive pages are moved from the RAM to the swap space.
Swap space can take the form of either a dedicated swap partition or a swap file. In most cases, when running Linux on a virtual machine, a swap partition is not present,
 so the only option is to create a swap file.

sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
/swapfile swap swap defaults 0 0 # add this in /etc/fstab
sudo swapon --show
sudo swapoff -v /swapfile
sudo rm /swapfile

Reboot
## reboot/shutdown/boot

/usr/lib/systemd/system		#where all systme target files are located here, system will first check this dir
/etc/systemd/system    		#its additional config file like apache,custom config fiel
we will have default.target symlink in thid dir so wen ever this target is changed this symlink is updated

shutdown -r +5	will reboot in 5min	#number of miniutes t wait before reboot this will send wall message
shutdown -c 		#to cancel reboot
w		# to check who is login
shutdown -r 00:00		#schedulet to reboot at nite 12 oclk
systemctl halt/halt/shutdown -h /shutdown -h now  #shutdown command
Boot Process
Boot Porcess?

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
---------------------------------------------------------
q) to change from old to new kernel for initial boot

check the gru2.cfg file 
awk -F\' '$1=="menuentry " {print $2}' /etc/grub2.cfg

grub2-set-default 3
grub2-mkconfig -o /boot/grub2/grub.cfg
shutdown -r now

q) how to recover grub failure?
https://www.youtube.com/watch?v=z047gbYCiWo&feature=youtu.be
Reinstalling the Boot Loader

when grub file is removed/damaged then system will not boot so and it ll go to 
grub console
grub>
	exit from grub console	#when u type exit it will take it to maintenance mode
	go to maintenance mode
	set boot from cd/dvd/usb
	then go to rescue centos filesystem> then it will open rescue mode
	then select option to rescue more (1)
	chroot /mtn/sysimage	#to change the console as root enviroment 	
	grub2-install /dev/sda
	grub2-mkconfig -o /boot/grub2/grub.cfg

Boot the system from an installation boot medium.
Type linux rescue at the installation boot prompt to enter the rescue environment.
Type chroot /mnt/sysimage to mount the root partition.
Type /sbin/grub-install bootpart to reinstall the GRUB boot loader, where bootpart is the boot partition (typically, /dev/sda).
Review the /boot/grub/grub.conf file, as additional entries may be needed for GRUB to control additional operating systems.
Reboot the system.


mount |grep -i ^dec

q)reseting root password

boot the system in rescuemode/recovery mode and 
go to shell
now the system will be read mode to enable it in write mode
moune -o rw,remount/
passwd
shutdown -r

q)inode
https://www.slashroot.in/inode-and-its-structure-linux#:~:text=Whenever%20a%20user%20or%20a,found%20from%20the%20inode%20table.

```

