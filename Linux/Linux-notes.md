


# Linux Kernal


# Working With Hardware
```
when linux os boots up numeros option will display on screen this msgs also contians logs form device 
dmesg       #tool used to display kernal msg from area in kernal called ringbuffer
dmesg | grep -i usb

udevadm     # is a managment tool for udev
udevadm info  --query=path --name=/dev/sda5  # is to query database for device information
udevadm monitor   #listen to kernal for new events it is usefull to identify newly attached device 

lspci       # list pci , displays all pci in system


lsblk       # list info about block device

lscpu       # display cpu info

lsmem  --summary     # Display mem info 
free -m             # display mem info

lshw                # display detailed info of haredware
```


## Security And Permission
### 1) Linux Accounts
```
cat /etc/passwd     #info about user account
cat /etc/group      # info about group 
```

each user has username and unique ID,gid & home directory,default shel, if no group is specfied then it will assign same id as uid
we can check this by using
```
id bob
```
Account Types:
1)user account
2)super user: is this user which has all access and its uid is 0
3)system user: like ssh mail and uid is 100 0rbetween 500 to 1000, this as softwer which dosent requre super user
4)service accoutn: like nginx


```
who     #To check who has login 
last    # to c last login and date and time of reboot
```
####  switching user(this will ask fo rpassword)

```
su 
su -c 
```

Default Config for sudo is defined in Sudoers File

```
cat /etc/sudoers #only the users which have entry on this file can use sudo command
```
if user is set to no login then no one can login using root user and passowrd
```
grep -i ^root /etc/passwd

syntax of sudores file

lines start with "%" are groups and other are users
User Privilege Lines
The fourth line, which dictates the root user’s sudo privileges, is different from the preceding lines. Let’s take a look at what the different fields mean:

root   ALL=(ALL:ALL) ALL
The first field indicates the username that the rule will apply to (root).
root ALL=(ALL:ALL) ALL
The first “ALL” indicates that this rule applies to all hosts.
root ALL=(ALL:ALL) ALL
This “ALL” indicates that the root user can run commands as all users.
root ALL=(ALL:ALL) ALL
This “ALL” indicates that the root user can run commands as all groups.
root ALL=(ALL:ALL) ALL
The last “ALL” indicates these rules apply to all commands.

<user> <hosts>=(users:groups)<commands>
```
sudo visudo

###  2) User Managment

```
useradd bob   # to create  new user
grep -i bob /etc/shadow
passwd bob    # to set password
whoaim    # to check uid
useradd -u 1009 -g 1009 -d /home/bob -s /bin/sh -c "comments" -e Expiy data -G <create user with multiple secondry group>      # with options

```
