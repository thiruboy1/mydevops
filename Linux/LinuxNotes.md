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

* Private/Public key based authentication: This method uses a private/public key combination for user authentication. The user on the client has a publickey and the server stores the corresponding private key.

When user tries to login, the server prompts the user to enter the key and lets the user login if the key is validated.


* Challenge response authentication: This method is based on response to one or more  challenge questions that the user has to answer  correctly in order to gain login access to the server.


* Password based authentication: Server prompts the user to enter their password. It checks the password against the stored entry in the /etc/shadow file and allows the user to login if the password is confirmed.


































