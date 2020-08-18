## Inventory

you can add alias to inventory files

web ansible_host=server1

## Variables:

variable stores info with each host
in playbook we can mention variable and to use variable use it with '{{ dns_server }}'
```
- hosts: all
  vars: 
    dns_server=10.200.20.39
```
### using variable to retrive the result of running command
if you want to use variable from previous task then ,
to add output of first task we use debug module so u can capture output of first task and pass it to second command
you can do this by using 
```
- hosts: all
  vars: 
    dns_server=10.200.20.39
  tasks:
  - shell: cat /etc/hosts	
    register: result
  - debug:
    var: result
```
### Magic Variables

to extract variables defined in one host to another host we can use magic varialbes
```
'{{ hostvar['web2'].ansible_host }}'
'{{ hostvar['web2'].ansible_facts.architecture }}'
'{{ hostvar['web2'].ansible_facts.devices }}'
'{{ hostvar['web2'].ansible_facts.devices }}'

````

### Magic Variable-Groups Names
msg: '{{ group_names }}' #this will return the group names in host inventory file it dosnet return host names

msg: '{{ inventory_hostname }}' # this will return hostnames not group names


### Jinj2 Template

in order to use ansible fact variable like hostname  in html page we can use following
```
- hosts: web
  tasks:
    template:
      src: index.html.j2 
      dest: /var/www/nginx-default/index.html
    
```
index.html.j2
```
<html>
this is my host name {{ inventroy_hostname }}
</html>
```

ansible-playbook pl.yaml --start-at-task "start httpd service" # this will start at this task and eignore all above task
optional u can tag your playbook and u can mention the tag on command like
"ansible-playbook pl.yaml --tags "install"
or u can skip task 
"ansible-playbook pl.yaml --skip-tags "install"

by default ansible will gather facts to disable facts u can mention 
```
"gather_facts: no" in play book.yaml
```
##configuration file
```
default config file is created in /etc/ansible/ansible.cfg
ansible-config list # list all configuration
ansible-config view # shows the current config file
```
```
ansible    -m        ping     all
<ansible><module><module name><host>
ansible    -a     'cat /etc/hosts'   all
<ansible><command>     <value>	     <host>
ansible -m setup localhost #nsible command to gather facts of the localhost
ansible -m ping -i /home/thor/playbooks/inventory all
ansible -m command -a date -i inventory web1 #Run an adhoc command to run a command on host web1 to print the date
```
##Privilage Esclation
```
become: yes #this will assume it as root user like sudo 
by default method used is sudo if u want to change this then u can use  following
become_methode: thiru
you can also set the in inventory file like follwig
/etc/hosts
web1=10.200.20.1 ansible_user=admin ansible_become=yes ansible_become_user=nginx

anything passed in command line has highest priority
anyting passed in default ansbile.cfg file has lowest priority
```

###modules

package module
```
- hosts: web1
  tasks:  - name: Install httpd package
    yum: name=httpd state=installed
```

```
- hosts: web1
  tasks:
  - yum:      name: http://mirror.centos.org/centos/7/os/x86_64/Packages/wget-1.14-18.el7_6.1.x86_64.rpm
      state: present
```

```
- hosts: all
  tasks:
    - name: Install unzip package
      yum:
        name: unzip
        state: present
```

```
- hosts: all
  tasks:
    - name: Install iotop package
      yum:
        name: iotop
        state: latest
```


## service module

```
- hosts: web1
  tasks:
  - name: install httpd
    yum:
      name: httpd
      state: present
  - name: start httpd service
    service:
       name: httpd
       state: started
```

```
---
- hosts: all
  gather_facts: no
  tasks:
    - name: Copy Apache welcome file
      copy:
        src: index.html
        dest: /var/www/html/index.html
    - service:
        name: httpd
        state: reloaded
```
firewalld module

```
- hosts: web1
  tasks:
   - firewalld:
      source: 172.20.1.101
      state: enabled
      zone: internal
      permanent: yes
      immediate: yes
```
zone:block
```
---
- hosts: web1
  tasks:
    - firewalld:
        port: 161/udp
        zone: block
        permanent: yes
        immediate: yes
        state: enabled
```


On web1 node add firewall rule in internal zone to enable https connection from Ansible controller machine and make sure that rule must persist even after system reboot. You can create a playbook https.yml under ~/playbooks/ directory.
IP address of ansible controller is 172.20.1.2.
```
---
- hosts: web1
  tasks:
    - name: Enable HTTPS for ansible controller
      firewalld:
        source: 172.20.1.2
        service: https
        zone: internal
        state: enabled
        permanent: yes

    - service:
        name: firewalld
        state: reloaded
```

```
---
- hosts: web2
  tasks:
    - name: Install pkgs
      yum:
        name: httpd, firewalld
        state: present

    - name: Start/Enable services
      service:
        name: "{{ item }}"
        state: started
        enabled: yes
      with_items:
        - httpd
        - firewalld

    - name: Change Apache port
      replace:
        path: /etc/httpd/conf/httpd.conf
        regexp: "Listen 80"
        replace: "Listen 8082"

    - name: restart Apache
      service:
        name: httpd
        state: restarted

    - name: Add firewall rule for Apache
      firewalld:
        port: 8082/tcp
        zone: public
        permanent: yes
        state: enabled

```
lvg module

```
---
- hosts: node00
  tasks:
  - name: create VG
    lvg:
      vg: vg_sql
      pvs: /dev/vdb1
```
lvm
```
---
- hosts: node00
  tasks:
    - name: create logical volume
      lvol:
        vg: vg_sql
        lv: lv_data
        size: 500M
```
filesystem modules

```
---
- name: Create file perm.txt
  hosts: web1
  tasks:
   - name: Create file perm.txt
     file: path=/opt/data/perm.txt mode=0640 state=touch
```

```
--
- name: Add block to index.html
  hosts: web1
  tasks:
   - blockinfile:
      owner: apache
      group: apache
      insertbefore: BOF
      path: /var/www/html/index.html
      block: |
       Welcome to KodeKloud!
       This is Ansible Lab.
```

```
---
- name: replace port 80 to 8080
  hosts: web1
  tasks:
  - replace:
      path: /etc/httpd/conf/httpd.conf
      regexp: 'Listen 80'
      replace: 'Listen 8080'
  - service: name=httpd state=restarted
```

archive modules
```
---
- name: Zip archive opt.zip
  hosts: web1
  tasks:
   - archive:
       path: /opt
       dest: /root/opt.zip
       format: zip
```

```
- name: extract local.zip to web1
  hosts: web1
  tasks:
  - unarchive:
      src: local.zip
      dest: /tmp
```

```
- hosts: web1
  tasks:
  - name: extract
    unarchive:
       src: local.zip
       dest: /tmp
```

```
- name: Compress multiple files
  hosts: web1
  tasks:
  - archive:
     path:
      - /root/file1.txt
      - /usr/local/share/file2.txt
      - /var/log/lastlog
     dest: /root/files.tar.bz2
     format: bz2
```

```
- name: Install and configure nginx on web1
  hosts: web1
  tasks:
  - name: Install nginx
    yum: name=nginx state=installed
  - name: Start nginx
    service: name=nginx state=started enabled=yes

  - name: Extract nginx.zip
    unarchive: src=/root/nginx.zip dest=/usr/share/nginx/html remote_src=yes

  - name: Replace line in index.html
    replace:
     path: /usr/share/nginx/html/index.html
     regexp: This is sample html code
     replace: This is KodeKloud Ansible lab
```

```
cron module
---
- name: Create a cron job to clear last log
  hosts: node00
  tasks:
   - name: Create cron job
     cron:
       name: "Clear Lastlog"
       minute: "0"
       hour: "0"
       job: echo "" > /var/log/lastlog
```


```
---
- name: Create a cron job to run free.sh script
  hosts: node00
  tasks:
   - name: Create cron job
     cron:
       name: "Free Memory Check"
       minute: "0"
       hour: "*/2"
       job: "sh /root/free.sh"
```

```
---
- name: remove cron job from node00
  hosts: node00
  tasks:
  - name: Remove cron job
    cron:
      name: "Check Memory"
      state: absent
```

```
- name: Creates an entry like "@reboot /some/job.sh"
  cron:
    name: "a job for reboot"
    special_time: reboot
    job: "/some/job.sh"
```

```
---
- name: Create cron for yum
  hosts: node00
  gather_facts: no
  tasks:
    - name: Creates a cron
      cron:
        name: yum update
        weekday: 0
        minute: 5
        hour: 8
        user: root
        job: "yum -y update"
        cron_file: ansible_yum
```

## users

```
---
- hosts: all
  gather_facts: no
  tasks:
    - group:
        name: 'admin'
        state: present
    - user:
        name: 'admin'
        uid: 2048
        group: 'admin'
```

this one use epoch time
 Sunday, December 31, 2023 11:59:59 PM GMT== 1704067199 
```
---
- hosts: all
  gather_facts: no
  tasks:
    - user:
        name: 'neymarsabin'
        expires: 1704067199
```

```
---
- hosts: all
  gather_facts: no
  tasks:
    - user:
        name: 'admin'
        state: absent
    - group:
        name: 'admin'
        state: absent
```

### Parallelism
when playbook are executed on multiple servers then ansible waits till each tasks completes on all servers,
suppose if any one servers is slow then ansible will wait till it completes so if u want to over come this then u can use "liner stratgey"
```
2 Types of stratgey r ther
a)linear strategy	(default strategy)
b) free strategy 	# all task runs independently 
c)serial:3		# we can decide how many servers can be processd similitenously
```
by default ansible will run only 5 servers at a time if u want to change this then update the 
forks = 5 in ansible.cfg
