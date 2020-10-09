# Terraform
## Start Guid
```
create terraform directory
create terraform file with .tf extension and terraform will read all the file in this folder
```
## Terraform Commands
```
terrraform version
terraform init		# to initilize , when ever new provider is added we need to initilize so that required files will be downloaded in the local folder
terraform plan		#terraform plan will read the .tf file and will tel wat all be done
terrafrom plan will run terraform refresh automaticaly
terraform apply 	# this will create the resource for specfied .tf file
terraform apply -auto-approve # this will auto approve 
terraform console	# to login to terraform console
terraform show		# this command will show the current state
terraform init
terrafrom apply
terrafrom destory 	to delete all created instance
terraform plan # testing infrasture, this will look the terrafrom file and will wat it will do without applying to infrastructure
terraform plan -out out.terraform # this will output to file, the changes going to make wil be saved inthis file
terraform apply out.terrafrom # its always recomendod to use this as it will show the changes
terraform validate #is used to check weither syntax is correct or not
terraform fmt		#is used to format the code
terraform workspace show
terraform workspace list
terraform workspace new
terraform workspace delete

```
## To destory created resources
```
terraform destory
terraform destory -target aws_instance.web	#insted of deleting all the resource we can specfiy the particular resource 

2nd way is commenting the to code in .tf file and run terraform plan and apply, then terraform will check the .tf  file and which ever resources is not ther it will remove  
```

## Terraform State File

```
terraform.tfstate	
```
* this wil have current state of infrastructure terraform will store states of infracture that is being created from tf files
eg: if u destory the resource then same will be updated in the state file , then if u run terraform plan then terraform will recreate the resource
* manualy if u change the instance type in aws console then if run terraform plan then terraform will check the tf file and aws status and then it will notifiy 
with ~ on command prompt and it indicates that follwing has been changed if u run terrafom apply then whatever is on tf file will be applied

## Terraform State File-Desired State and Current State

1) Desired State: its the state which is mentioned in the file
2) Current State: current state

terraform will alway try to match the desired state with current state

if resources is not mentioned in the tf file eg: security group then if SG is update in the  aws console then if u run the terraform plan then terraform will notifity the changes coz terraform will monitor only state which is mentioned in tf file 

## Terraform Provider Versionin

provider will have multiple versions,if version is not mentioned int  the .tf file then terraform will assume most recent version, so for production its mandatory to mention the version 
```
provider "aws" {
	region = "ap-south-1"
	version = "2.7"
}

version >="2.7"
version < "2.7"
version ~> "2.0"	#any version in 2x range
version >=2.10,<=2.30	#any version bw 2.10 and 2.30
```

## Types of terraform provider

1) hasicorp distributed	# developed and tested by hasicorp
2) 3rd party		# developed by 3rd party, which cannto be downloade automaticaly, insted we need to install mannually install thirdparty providers by placing their plugin exe in the following direcotry
windows: %APPDATA%\terraform.d\plugins
all other: ~/.terraform.d/plugins

# Read Generate Modify Configuration

## Terraform Attributes and Outputs

* After terraform apply, the terraform will create the ec2 instance if u want to c the ip address of ece then u have to  login to console and note down the ip 
* but in terraform you can output the variable so that there is no need to login to console

*The outputed attributes can not oly be used for the user ref but it can also act as input to  other resources being created via terraform 

for eg: after EIP gets created its ip should get whitleised in SG this in one most advantage of attibues and output
 
## Refrencing cross account resource attributes

1) create EIP & EC2 and associate Eip with EC2
2) create EIP & associate with Security Group

## Terraform Variables

To use variable in terraform we use following keyword insted defining the attribute on multiple location, we can create a single variable and  refrence that variable to multiple location so if there is any change in attribute just we need to change variable file

varialbe are stored in variable.tf file same project structure and
```
variable "ip"{
	default = "10.20.20.20/32"
}
```
 refrence them in ur file using var.ip

## Variable Assignemnt
```
1) Env Variables
	windows:
		setx TF_VAR_instancetype t2.micro (where setx is windows command and TF_VAR is variable keyword
2) Command Line Flags
	if u remove the default value then terraform will ask for value in cli
variable can be explictly specfied in command line
terraform plan -var="instancetype=t2.small"

3) From File
	##terraform.tfvars (this file name is very important, 
and also u can define custom file name and define explctly in cli terraform plan -var-file="custom.tfvars"
insted of defining the variable in command line u can defin the same in terraform.vars
instancetype="t2.small"

4) Variable Defaults: 
	this type of variable are defind in variables.tf file if no explice variable are specfied
then it will access this default variable ,and it can be accessed in 
.tf file using var.variable name.value

variable "instancetype" {
	default = "te.micro"
}

	


```

## Data type for Variables:

when ever user reades templeats , its difficult to read withot types in the 
variable to its better to mention type in variable
```
Number:
variable "number"{
	type = number
	
}


string
variable "myvar" {
	type = "string"
	default = "hello"
}

variable "mymap" {
	type = map(string)
	default = {
 		mykey = "myvalue"
	}
}
variable "mymap" {
	type = list
	default = [1,2,3]
}


```
## Fetchig data from map and list in variables
MAP
```
resource "aws_instance" "ec2" {
  ami = var.ami
  instance_type = var.ttypes["ap-south-1"] #Extracting data from map variable

}

variable "ami" {
  default = {
    ami = "ami-0e306788ff2473ccb"
  }
}

variable "ttypes" {
  type = map
  default = {
    ap-south-1 = "t2.micro"
    ap-south-2 = "t2.nano"
  }
}
```

## after loging to console to check variable run following
```
> var.myvar
> "${var.myvar}"
> var.mymap
> var.mymap["mykey"]
>var,mylist
>var.mylist[0]
>element(var.mylist,1)	#function 
>slice(var.mylist, 0,2)
```

## resources.tf=>
## variable can be defined in same file are in seperate file
```

provider "aws"{

}
```

```
variable "AWS_REGION" {
	type = string

 }
variable "AMIS" {
	type = map(string)
	default = {
	eu-west-1 = "my ami"
		}

 }

resource "aws_instance" "example1"{
	ami = var.AMIS[var.AWS_REGION]
  	instance_type = "t2.micro"
}
resource "aws_instance" "example2"{
	ami = var.AMIS[var.AWS_REGION]
  	instance_type = "t2.micro"
}


```
## u can also define variable in terrafrom.tfvars
```
cat terraform.tfvars
terraform.tfvars
AWS_REGION="eu-west-1"
```
* wen ever u change provider or moudle or plugin u need to initilize the terraform > terrafrom init

>terrafrom console
>var.AMIS[var.AWS_REGION]

string
nubmer
bool
```
variable "a-string" {
	type = string
 }
variable "a-number" {
	type = number
 }
variable "a-bool" {
	type = bool
 }
```
## terraform complex
```
list	list:[1,2,4]
set	#unique values
map	# map:{"key" = "value"}
object  # is like map 
tuple	#tuple is like list but each element can be diffrent type [1,"stirng",false]

```
### variable
use variable to hide secrets like aws key
use variable for element that might change like ami
```
provider.tf
provider "aws" {
  access_key = "${var.AWS_ACCESS_KEY}"
  secret_key = "${var.AWS_SECRET_KEY}"
  region     = "${var.AWS_REGION}"
}

vars.tf
variable "AWS_ACCESS_KEY"{}
variable "AWS_SECRET_KEY"{}
variable "AWS_REGION"{
	default = "eu-west-1"
	}
variable "AMI" {
	type = "map"
	default = {
	eu-east = "ami-12qw3"
	us-west = "ami---"
	eu-west1 = "ami ---"
	}
}
instance.tf
resource "aws_instance" "example" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"
}

terraform.tfvars  # put this file in gitignore
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
AWS_REGION = ""


```

## Count And Count INDEX
Count Parameter: count parameter is used to increament the number or to scale the resources this count = 5 will create 5 ec2 instance in the name of ec2-1[0],ec2-1[2]...,ec2-1[4]
```
resource "aws_instance" "ec2-1" {
  ami = var.ami
  instance_type = var.ttypes["ap-south-1"]
  count = 5
}
```
### Count.index: will allows us to fetch the index of each iteration in the loop
```
resource "aws_instance" "ec2-1" {
  ami = var.ami
  name = "ec2-1.${count.index}"
  instance_type = var.ttypes["ap-south-1"]
  count = 5
}
insted of mentiong the numbers in name u can create list then use list index 
variable "elb_names"{
	type=list
	default=["dev","qa","prod"]
}
resource "aws_instance" "ec2-1" {
  ami = var.ami
  name = var.elb_names[count.index]
  instance_type = var.ttypes["ap-south-1"]
  count = 5
}
```
## Conditional Expressions: it check for the condition ifts true then it assigns true value
if false then it assigns false value
```
condation ? true_value:false_value

variable "istest"{}
resource "aws_instance" "dev" {
  ami = var.ami
  instance_type = var.ttypes["ap-south-1"]
  count = var.istest == true ? 1 : 0

}

```
## if istest is true then set count = 1 else count is 0
```
resource "aws_instance" "prod" {
  ami = var.ami
  instance_type = var.instancetype[1]
  count = var.istest == false ? 3 : 0


}
```

## Local Values: 
assignes a name to expressin , allowing it to be used multiple times within  a moduel without repeating it


## Terraform Functions: 
Terraform langauage includes number of built in functions we must use terraform built in functions only we cannot create custom functions
Syntax:
max(5,12,9)
12
```
1)numeric
2)string
3)colletion
4)encoding
5)filesystem
6)data and time
7)hash and crypto
8)ip network
9)type conversion
```

```
ami = lookup(var.ami,var.region)
      lookup(map,key,default)
tags = {
	name = element(var.tags,count.index)
}

functions are called with syntax name(arg1,arg2..) and wrapped with ${..}
file:
${file("mykey.pub")} this will read the contents of pub file

date & Time Function:

```
## Data Sources
Data Sources allow data to be fetched or computed for use elsewhere in terraform 
config file
each region will each ami-id if u use another region ami id to mumbai then we will get error
so to address this we have to hard code the ami-id but ami-id will be keep on changing
so we can use data sources,

1)data source must be defined under data block
2)reads from specfic data source eg: aws_ami and exports results under "app_ami"
```
data "aws_ami" "app_ami"{
	most_recent = true
	owner = ["amazon"]
}
```
and the above block will get multiple ami so to filter the requried ami we use follosing

```
filer{
	name = "name"
	values= ["amzn2-ami-hvm*"]

}
```
and to use the result in .tf file we use the followig
```
resources "aws-inst"{
	ami = data.aws_ami.app_ami.id

}

```
## Debugging In Terraform
terrafrom has detaild logs which can be enabled by setting the 
TF_LOG env variable to any value
TF_LOG can be set to any one of this varialbe
```
1)TF_LOG = TRACE
TF_LOG = DEBUD
TF_LOG = INFO
TF_LOG = WARN
TF_LOG = ERROR
```
in order to redirect the log to file we can use 
TF_LOG_PATH=/tmp/terrafrom-crash.log now logs will not be displayed in cmd prompt but it will be stored in file


## Terraform Fromat

terraform fmt # this command allows us to reformating the code 
indentation will be done properly

## Validating Terraform Configuration Files
terraform validate #
Terraform Validate Primarily check wether a confi is syntactically is valid
it checks various aspects including unsupported arguments undeclared variables and others

## Load Order & Semantics
Terraform Generally loads all the config file witin the directory specfied in 
alphabetical order

the files loaded must be in either .tf or .tf.json to specfiy the format that is in use

in production its recomended to create seperate file for variable and provdier,ec2,iamuser ..etc so that for 
reading it will be cleaner

resource or variable name must be unique

## Dynamic Blocks
in many of the use case there are repeatable nested blocks that needs to be defined
this can lead to a long code and it can be difficult to manage in longer time
for eg: if we need 40 ingress security group insted of defining multiple 
security group we can use dynamic block.

Dynamic block allows us to dynamically construct repetable nested blocks which is supported inside
resource,data,provider,and provisioner blocks:

```
variable "sg_ports" {
  type        = list(number)
  description = "list of ingress ports"
  default     = [8200, 8201,8300, 9200, 9500]
}

resource "aws_security_group" "dynamicsg" {
  name        = "dynamic-sg"
  description = "Ingress for Vault"

  dynamic "ingress" {
    for_each = var.sg_ports
    iterator = port
    content {
      from_port   = port.value
      to_port     = port.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  dynamic "egress" {
    for_each = var.sg_ports
    content {
      from_port   = egress.value
      to_port     = egress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```
## Tainting Resources
you have created new resources via terraform
user have made lot of manual changes(both infra and inside server) due this its not working as 
expected when ever u do terraform plan u get lot of errors, so we have two ways to deal this 

```
1) Import the changes to terraform
2) Delete and recreate the resources

```
2) delete and recreate the resource
the terraform taint command manually marks a terraform managed resource as tainted , forcing it to 
be destoryed and recreated on the next apply
when u do terraform plan then terraform will delete the resource and recreat from scratch

```
terraform taint aws_instance.myec2	#this command will taint and it will be recreated
for next terraform plan & terraform apply
```
you can check the same in terraform state file
* terraform taint will not modifiy the infra insted it will modfiy state file, to modifiy u have to run terraform apply
* once resource is marked as tainted the next plan will show that the resource will be detroyed and recreated and 
the next apply will implement this change
 
## Splat Expressions

Splat Expression allows us to get list of all the attributes
(*) for all

```
resource "aws_iam_user" "lb" {
  name = "iamuser.${count.index}"
  count = 3
  path = "/system/"
}

output "arns" {
  value = aws_iam_user.lb[*].arn
}
```
 

## Terraform Graph
* The Terrafrom Graph command is used to generate a visual representation of either a config or execution plan
* the output of terraform graph is in the dot format which is easyily converted to an image
```
terraform graph > graph.dot
yum install graphviz
cat graph.dot | dot -Tsvg > graph.svg
```
* output will be in dot format file , in order to read this u need use graphiviz or online graphiz and paste the code


## Saving Terraform Plan to File
The generated terraform plan can be saved to specfic path
this plan can then be used with terraform apply to be certain that only the changes show in this plan are appplied

```
terraform plan -out=demofile	#created file will be binary file, u cannot read directly 

terraform apply demofile
```

## Terraform Output
The Terraform output command is used to extract the value of an output variable from state file

```
terraform output a
```
u can c output values in 3 ways
1) terraform apply 
2)terraform.tfstate		# inspect tfstate file
3)terraform output iam_arn		#makeuse this command

## Terraform Settings
the special terraform config block type is used to confgure some behaviours of terraform 
iteself such as requiring a minium terraform version to apply your config
 terraform settings gathered togther into terraform blocks:

terraform {
	required_version = ">0.12.0	# tells which version to be used if it use version below this then it wil throw error
	required_provider {
		mycloud = {
		source = "mycorp/mycloud"
		version = "~> 1/0"
		}
	}

}


## Dealing with Large Infrastructure
```
when ur dealing with larger infra like 100s of sg ec2 then u may reach api limit, then ur request will not be serverd
so to avoid u do the following
1) insted of definig all the infra in one code define in each seperate file like(ec2,rds,iam,sg..etc) in this case only 
requried resources need to be refreshed not all resources,
advantage is each can be applied independently

* wen u run terraforma plan then terraform will fetch state of all resource, 
if u want avoid this run the follwoing
terraform plan -refresh=false
2)the -target=resource flag can be used to targer specfic resource
2terraform plan -target=ece

```
# Terraform Provisioners

* Terraform Provisioners will allow us to install a specfic configuration eg: installing nginx , on ec2 instance
* so once ec2 is created application will be automatical configured
* provisioners are used to execute scripts on local or remote machine as part of resource creation or destruction

eg: on creation of web server execute a script which install nginx webserver

## Types of Provisioners
```
1) local-exec	#this will run the command on local machine(terraform machine)
		this is mainly used to execution of ansible playbooks
2) remote-exec	# this will execute the commands on remote machine

```

## remote-exec
The remote-exec provisioner invokes a script on a remote resource after it is created. This can be used to run a configuration management tool, bootstrap into a cluster, etc. To invoke a local process, see the local-exec provisioner instead. The remote-exec provisioner supports both ssh and winrm type connections.


* first you have to make sure that remote resource are created first
* provisioner connection #u need to mention ssh-key ,in order to install webserver   

### Example usage
```
resource "aws_instance" "myec2" {
   ami = "ami-082b5a644766e0e6f"
   instance_type = "t2.micro"
   key_name = "kplabs-terraform"

   provisioner "remote-exec" {
     inline = [
       "sudo amazon-linux-extras install -y nginx1.12",
       "sudo systemctl start nginx"
     ]

   connection {
     type = "ssh"
     user = "ec2-user"
     private_key = file("./kplabs-terraform.pem")
     host = self.public_ip
   }
   }
}
```
### Script Arguments
```
resource "aws_instance" "web" {
  # ...

  provisioner "file" {
    source      = "script.sh"
    destination = "/tmp/script.sh"
  }

  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/script.sh",
      "/tmp/script.sh args",
    ]
  }
}
```
## Local-exec
The local-exec provisioner invokes a local executable after a resource is created. This invokes a process on the machine running Terraform, not on the resource

one of the most used approch of local-exec is to run ansilbe-playbook on the created server after the resource is created

### Example Usage
```
resource "aws_instance" "web" {
  # ...

  provisioner "local-exec" {
    command = "echo ${aws_instance.web.private_ip} >> private_ips.txt"
  }
}
```

## Creation-Time & Destory Time Provisioners

1) Creation Time Provisioner:
* creation time provisioner are only run during creation not duirng or any other lifecyclye 
* if a creation time provisioiner fails the resource is marker as tainted(resource will be deleted and recreated)

2) Destory time provisioner:
* Destory time provisoners are run before the resource is destoryed
* in real time we may need to remove the antivirus before deleting ec2 at this time we use destory time provisoners

```
provider "aws" {
  region     = "ap-southeast-1"
  access_key = "YOUR-KEY"
  secret_key = "YOUR-KEY"
}


resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    description = "SSH into VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    description = "Outbound Allowed"
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "myec2" {
   ami = "ami-0b1e534a4ff9019e0"
   instance_type = "t2.micro"
   key_name = "ec2-key"
   vpc_security_group_ids  = [aws_security_group.allow_ssh.id]

   provisioner "remote-exec" {
     inline = [
       "sudo yum -y install nano"
     ]
   }
   provisioner "remote-exec" {
       when    = destroy
       inline = [
         "sudo yum -y remove nano"
       ]
     }
   connection {
     type = "ssh"
     user = "ec2-user"
     private_key = file("./ec2-key.pem")
     host = self.public_ip
   }
}
```

## Failure Behavior for Provisioners
* By default provisoners that fail will also cause the terraform apply itself to fail
* the on_failure settings can be used to change this the allowed values are

```
continue:	ignore the errot and continue with creation or destruction
fail:		raise an error and stop applying(the default behaviour) if this is a creation provisioner , taint resource
```

```
resource "aws_instance" "web"{
	#......
	provisoner "local-exec" {
	 	command = "echo ther server $(Self.private_ip)"
	on_failure = continue
	}
}
```

# Terraform Moudules & Workspaces

## Understanding DRY Principle
in software engi DRY(dont repeat yourself) is a principle of software development aimed at reducing repetition of software patterns

in the earlier lecture we were making static content into variable so that there can be single source of information

insted of repeting code each time, we can define the cetrilized location and we can use the same as modules


## Implementing EC2 module with Terraform
create module directory & place ec2 code

module>ec2>ec2.tf
```
resource "aws_instance" "app-dev" {
  ami           = "ami-0e306788ff2473ccb"
  instance_type = "t2.micro"
}
```

project>myprj>myec2.tf

```
module "ec2modules" {
  source = "../../modules/ec2/"
}
```

## Variables and Terraform Modules
* we will have multiple enviroments like development,production,staging, each of them may require diffrent
configuration of ec2 since we have encoded in moudle we cant change 
* if paramaters (instance_type = "t2.micro")is hardcoded in the module the u cannot change 

so in order to overcome the above issue we can use variables


moudle>ec2>variables.tf
```
variable "instance_type"{
	default = "t2.micro"
}
```

module>ec2>ec2.tf
```
resource "aws_instance" "app-dev" {
  ami           = "ami-0e306788ff2473ccb"
  instance_type = var.instance_type.
  
}
```
project>myprj>myec2.tf

```
module "ec2modules" {
  source = "../../modules/ec2/"
  instance_type = "t2.large"
}
```
* you can make any paramater as variable so that end use can define

## Terraform Registry
Terraform Registrh is a repository of moudle wiriten by the terraform community
fetchin module directly from terraform registert
```
module "ec2-instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "2.15.0"
  # insert the 10 required variables here
}

```


## Terraform Workspace
* Terraform allows us to have multiple workspaces with each of the workspace we can have diffrent set enviroment variable associated
* staging will have instance-type = t2.micro and production instance-type = large
so when u switch from staging to production workspace then it will automatical change instance type large

terraform workspace show
terraform workspace list
terraform workspace new
terraform workspace delete

## Implementing Terraform workspace

```
provider "aws" {
  region     = "us-west-2"
  access_key = "YOUR-ACCESS-KEY"
  secret_key = "YOUR-SECRET-KEY"
}

resource "aws_instance" "myec2" {
   ami = "ami-082b5a644766e0e6f"
   instance_type = lookup(var.instance_type,terraform.workspace)
}

variable "instance_type" {
  type = "map"

  default = {
    default = "t2.nano"
    dev     = "t2.micro"
    prd     = "t2.large"
  }
}
```

# Remote State Managment

## Integrating with GIT for team management

## Security Challenges in Commiting TFState to GIT

```
not recomended
* donot store the password in the .tf file insted store it in seperate file and use file(../../filename.txt) to import the passowrd
  but the problem is same password will be stored in terraform.tfstate file
```

## Module Sources in Terraform
The Source argument in module block tells terraform where to find the source code for the desired child module

1) local paths
```
A local path must begin with either ./or ../ to indicate that its a local path

module "consul"{
	source = "../consul"
}

```
2) Terrform Registry
3) GitHub
4) Bitbucket
5) Generic Git,Mercurial Repositories
6) HTTP URLs
7) s3 Buckets
8) GCS bUCKETS


### Generic Git Repository

* by default terraform will clone and use default branch in the repo,
* however you can overide this using ref argument
*Arbitrary Git repositories can be used by prefixing the address with the special git:: prefix. After this prefix, any valid Git URL can be specified to select one of the protocols supported by Git.

```
module "vpc" {
  source = "git::https://example.com/vpc.git"
}

module "storage" {
  source = "git::ssh://username@example.com/storage.git"
}

```

### GitHub
Terraform will recognize unprefixed github.com URLs and interpret them automatically as Git repository sources.
```
module "consul" {
  source = "github.com/hashicorp/example"
}

module "consul" {
  source = "git@github.com:hashicorp/example.git"
}
```

## Terraform and .gitignore
gitignore tells which files are not be uploaded
depending on env its redcomended to avoid commiting certian file to git
file to ignore

.terraform		#this file wil be recreated when terraform init
terraform.tfvars	# likely to contain sensitive data
terraform.tfstate	# should be stored in the remote side
crash.log	#if terraform crashes the logs are stored to a file named crash.log



## Remote State Management with Terraform

if i ignore the tfstate file and push to repo then how will u colabrate the work?
this can be done using remote backend 

* all the tf files will be stored in git and tfstate file will be stored in (S3)remote backend
Terraform Supports various types of remote backends which can be used to store state data
as of now we were storing state data in local and git repository
Depending on remote backends which is being used there can be various features

Two types of backend
1) Standard Backend:	State Storage and Locking 
2) Enhanced Backend: 	All feature of standard +Remote Managment

## Implementing S3 Backend
if u want to store the tfstate file in remote backend the u have to tell terraform

step 1) create s3 bucket
step 2) create backend.tf in samedirectory and mention the s3 bucket name ..etc
setp 3) run terraform init
setp 4) then all the tfstate file will be stored in s3 bucket



```
terraform {
  backend "s3" {
    bucket = "thiru-remote-backend-terraform"
    key    = "remote.tfstate"
    region = "ap-south-1"
    access_key = ""
    secret_key = ""
  }
}

```

## Challenges with State File locking
if two ppl are working on same project which has same backend then if two ppl wirtes the same
then state file will get corrupted, so to over come u must use locking machanisem

Whenever you are performing write operation terraform would lock the state file
this is very important as otherwise during your ongoing terraform apply operaton if others
also try for the same it would corrupt the state file

eg:-

person a is terminating the rds resoure which has associated rds.tfstte file
persion b is now tried resizing the same rds resource at same time

so this is why state file will be locked so that 2nd person perform wirte operation ,
then terraform will display error as" file is alredy locked"

* this locking feature is not avilable on all backends, eg:- S3

## Integrating DynamoDB with S3 for state locking
if you want tfstate file locking with s3 then u have use dynomodb
1) create dynomodb
2) primary key as LockID and create table
3) create backend file
4) terraform init
5) terraform plan
```
terraform {
  backend "s3" {
    bucket = "thiru-remote-backend-terraform"
    key    = "remote.tfstate"
    region = "ap-south-1"
    access_key = "AKIAUNKRSONDUGHACTBI"
    secret_key = "C3YkjqEHqqeeYZPfV1tN5qBbZu5OAtJiO1VDym4H"
    dynamodb_table = "dynomodb-statelock"
  }
}

```
## Terraform State Management
As your terraform usage become more advanced there are some cases where you may need to modify the terraform state
its important to never modifiy the state file directly make use of terraform state command

terraform state has multiple sub command

1) terraform state list #basicaly shows the resource created by state file
2) terraform state move
* the terraform state mv command is used to move items in as terraform state
* this command is used in many cases in which you want to rename an existing resource without destorying and recreating it
```
if u want to rename the ec2 then u can use "mv"
```
* due to destructive nature of this command, this command will output a backup copy of the state prior to saving changes

```
terraform state mv [options] source destination
terraform state mv aws_instance.webapp aws_instance.my-ec2

``` 

3) Terraform Pull:
(if backend s3)this command will pull the state form s3 and display is it 
The terraform state pull command is used to manally download and output the state from remote state
this is usefull for reading values out of state(poentially pairing this command with something like s=jq)

4) Terraform Push:
This command is used to manually upload a local state file to remote state
this command should rarely be used

5) Terraform rm:
the terraform state rm command is used to remove items from the terraform state
items removed from the terraform state are not physically destoryed
items removed from terrafor state are only no longer managed by terraform 
for eg: if u remove an aws instance from the state the aws instance will continue running but terrafrom plan will no longer see the instance
after removing the resource , if resources is present in .tf file then resource will be created again

6) terraform show:
this command is used to show the attributes of single resource in the terraform state
terraform state show aws_instance.webapp


## Importing Existing Resources with Terraform Import
if resource are allready created and u want maintain using terraform then u can use 
import to import he allready creted resources

till now if u want import the manual-resource then terraform will only create only state file not .tf file, then 
u have to create the resource manualy .tf file
mention all requried parameters in the tf file
```
resource "aws_instance" "example" {
  # ...instance configuration...
}
```
terraform import aws_instance.myec2.ec2-id
1) when u run import , terraform will first state file
2) then it ll map the state file with resource in .tf file


# Security Primer











## AWS 
1)create aws account
2)create access key and id

## spining EC2 in aws
instance.tf
```
provider "aws" {
  access_key = "ACCESS_KEY_HERE"
  secret_key = "SECRET_KEY_HERE"
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0d729a60"
  instance_type = "t2.micro"
}
```





## SOFTWARE PROVISIONING
ther are 2 way to provision software on your instance
1)custome ami and bundle your software with image
	packer is great tool to this
2)use standard image
	use file uploads or use remote exec or use automation tools like chef puppet ansible
chef is integrated
for ansible u first run terrafrom and ouput ip addrss and then run ansible-playbook

a)file upload
the provisioner may use ssh / u can use key pair mention in the file

provisoner "file" {
 source = "app.conf"
 destination = "/etc/myapp.conf"
 connection{
	user = "${var.instance_username}"
	password = "${var.instance_password}"
	}
}


##using ssh key pair

```
resource "aws_key_pair" "thiu-key" {
	key_name = "my_key"
  	public_key "ssh-rsa my-public-key"
}

resource "aws_instance" "example" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"
  key_name = "${aws_key_pair.mykey.key_name}"	


provisoner "file" {
 source = "script.sh"
 destination = "/opt/script.sh"
 connection{
	user = "${var.instance_username}"
	password = "${file(${var.path_to_private_key})}"
	}	
   }
provisoner "remote-exec"{
	inline= [
	"chomd +x /opt/script.sh"
	"sudo /opt/script.sh"
	]
	} 
}
```
## Terraform Attribute

terraform keeps attribute of all the resources you create
eg:aws instance public_ip this attribute can be queried and outputed you can use output to display the variable
```
output "ip" {
 value =  "${aws_instance.example.public_ip}"
}
```

## attribue in scripts
```
resource "aws_instance" "example" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"
  provisioner "local-exec"{
	command = "echo ${aws_instance.example.private_ip}" >> private.txt
	}
}	
```
## Remote State
```
terraform keeps the remote state of the infra 
it store it in a file called terraform.tfstate
there is also backup call terrafrom.tfstate.backup
when u execute terraform apply, a new terraform.tfstat and backupfile is created
this is how terrafrom keeps track of the remote state
eg: you terminate instance that is manage by terraform then aftet terrafom apply ti will be create again

terraform state can be saved remote using backend function in terraform
the default is local backend (local terraform state file)
other backends are s3, consul, terraform enteerprise
```
## configure remote state
```
1)add backend code to a backend.tf file
  a) run the init process

terrafom{
 backend "consul"{
 	 address = ""
 	 path = ""
	}
}
terrafom{
 backend "s3"{
	  bucket = " mybucket"
	  key = "terrform/proj"
	  region = "eu-west-1"
	}
}

```
## Data Sources

Data sources allow data to be fetched or computed for use elsewhere in Terraform configuration. Use of data sources allows a Terraform configuration to make use of 
information defined outside of Terraform, or defined by another separate Terraform configuration.



https://github.com/wardviaene/terraform-course/tree/master/demo-5
data will be pulled from aws and filter the regions and service will be ec2 and it will be 
sent to sg group
```
  
data "aws_ip_ranges" "european_ec2" {
  regions  = ["eu-west-1", "eu-central-1"]
  services = ["ec2"]
}

resource "aws_security_group" "from_europe" {
  name = "from_europe"

  ingress {
    from_port   = "443"
    to_port     = "443"
    protocol    = "tcp"
    cidr_blocks = data.aws_ip_ranges.european_ec2.cidr_blocks
  }
  tags = {
    CreateDate = data.aws_ip_ranges.european_ec2.create_date
    SyncToken  = data.aws_ip_ranges.european_ec2.sync_token
  }
}
```

## Template Provider

this can help creating customized configuration files you can build tempalte based on variables  for terraform resources

in if u want to send data to "user-data" in aws then u can use template provider


## Modules

modules makes terraform more organized
a)modules from git
```
moudle "module-example"{
	source = "github.com/adf/adsf"
}
```
b)modules from local folder
```
moudle "module-example"{
	source = "./moudle-example"
}
```
you can also pass atgumetns to module
```
moudle "module-example"{
	source = "./moudle-example"
	region = "us-west-1"
}
inside module folder u wiil have
module-example/vars.tf
module-example/output.tf
module-example/cluster.tf

```
### in main part of code use the output from the module
```
output "some-output" {
	value = "${module.module-example.aws.cluster}"
}
```

## Terraform With AWS
creating vpc
https://github.com/wardviaene/terraform-course/blob/master/demo-7/vpc.tf
https://github.com/wardviaene/terraform-course/blob/master/demo-7/nat.tf

##vpc
```
resource "aws_vpc" "vpc name" {

}
```
##  instance
```
resource "aws_instance" "instance name" {

}
```
## EBS
```
resource "aws_ebs_volume" "ebs-volume-1" {
  availability_zone = "eu-west-1a"
  size              = 20
  type              = "gp2"
  tags = {
    Name = "extra volume data"
  }
}

resource "aws_volume_attachment" "ebs-volume-1-attachment" {
  device_name = "/dev/xvdh"
  volume_id   = aws_ebs_volume.ebs-volume-1.id
  instance_id = aws_instance.example.id
}


```
## User Data

user data in aws can be used to do any customization at launch you can install extra software, prepare the isntance to join cluster,mount volumes

## AWS EIP


you can use aws_eip.eipname.public_ip attribute to show ip address after terraform apply
```
resources "aws_eip" "eipname" {
	instance = "${aws_instance.name.id}"
	vpc = ture
}
```
## Route53 
```
resource "aws_route53_zone" "newtech-academy" {
  name = "newtech.academy"
}

resource "aws_route53_record" "server1-record" {
  zone_id = aws_route53_zone.newtech-academy.zone_id
  name    = "server1.newtech.academy"
  type    = "A"
  ttl     = "300"
  records = ["${aws_eip.eipname.public_ip}"]
}
resource "aws_route53_record" "mail1-record" {
  zone_id = aws_route53_zone.newtech-academy.zone_id
  name    = "newtech.academy"
  type    = "MX"
  ttl     = "300"
  records = [
    "1 aspmx.l.google.com.",
    "5 alt1.aspmx.l.google.com.",
    "5 alt2.aspmx.l.google.com.",
    "10 aspmx2.googlemail.com.",
    "10 aspmx3.googlemail.com.",
  ]
}

output "ns-servers" {
  value = aws_route53_zone.newtech-academy.name_servers
}

```
##interpolation

### variables
```
string varialbe - "${var.somthing}"
map variable  	-  "${var.AMIS["us-east-1"]}", "${lookup(var.AMIS,var.AWS_REGION)}"
List Variable	-  "${var.subnets[i]}"
```
### various

```
outputs of moudle - ${module.aws_vpc.vpcid}
count information - ${count.index}
path information  - path.cwd(current directory), path.module(module path), path.root(root module path)

```
### math
```
add (+) (-) (*) (/)
eg: ${2+3*4}
```
## Conditionals

if else
```
condition ? tureval: falseval

resource "aws_instance" "myinstance"{
[...]

count = "${var.env == "prod" ? 2: 1}"

}
```
### 
```
Equlaity: == and !=
numerical comparasion : >,<,>=,<=
boolean logic: &&,||,unary !
```
demo-18

## Functions


for and for_each loop
```
[for s in ["this is a ","list"]:upper(s)]

```

	 
