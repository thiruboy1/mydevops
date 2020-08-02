


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
