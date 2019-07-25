# Deploying Nginx in kubernetes Cluster, using nfs volume

## What you will learn after this Excersis

```
* How to Create & Deploy Pod ?
* How to Create Service to access Pod ?
* How to Create NFS Server & Client ?
* How to Create shared Volume ?
* How to Create PV ?
* Hot to Create PVC ?
```
## Steps 
```
      Prerequests: NFS server
      Step1: create an object definition for the PV
      Step2: create an object definition for the PVC
      Step3: Creating the NGINX Pod
      step5: Creating Service to access NGINX pod 
```
## Prerequests- Installing NFS Server 
```
yum -y install nfs-utils nfs-utils-lib
chkconfig nfs on
service rpcbind start
service nfs start
echo -e "/root/share	10.200.20.245(rw,syncno_root_squash)" >> /etc/exports
exportfs -a
```
## Prerequests- Installing NFS Client On kubernets Master
```
yum -y install nfs-utils nfs-utils-lib -y
systemctl enable rpcbind &&
systemctl enable nfs-server &&
systemctl enable nfs-lock &&
systemctl enable nfs-idmap &&
systemctl start rpcbind &&
systemctl start nfs-server &&
systemctl start nfs-lock &&
systemctl start nfs-idmap 
mkdir -p /root/share
mount 10.200.20.250:/root/share /root/share/
echo -e "10.200.20.250:/root/share"  "/mnt/share nfs"      "auto,noatime,nolock,bg,nfsvers=3,intr,tcp,actimeo=1800 0 0">>/etc/fstab
showmount -e
```

## Step1- Creating object definition for the PV
nfs-pv.yaml
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
 capacity:
   storage: 1Gi
 accessModes:
   - ReadWriteMany
 persistentVolumeReclaimPolicy: Retain
 nfs:
  path: /root/share
  server: 10.200.20.250
  readOnly: false

```
### kubectl create -f nfs-pv.yaml
## Step2- Creating object definition for the PVC
nfs-pvc.yaml
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
   name: nfs-pvc
spec:
   accessModes:
   - ReadWriteMany
   resources:
     requests:
       storage: 1Gi
```
### kubectl create -f nfs-pvc.yaml
## Step3- Creating POD
```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx1
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx1
  template:
    metadata:
      labels:
        app: nginx1
    spec:
      containers:
        - image: "nginx:1.7.9"
          name: nginx1
          volumeMounts:
            - name: nfs-volume
              mountPath: /usr/share/nginx/html
          ports:
            - containerPort: 80

      volumes:
        - name: nfs-volume
          persistentVolumeClaim:
              claimName: nfs-pvc

```
### kubectl create -f nginx-deployment.yaml
## Step4- Creating Service

```
apiVersion: v1
kind: Service
metadata:
    name: nginx1-frontend
spec:
  type: NodePort
  ports:
   - targetPort: 80
     port: 80
     nodePort: 30000
  selector:
     app: nginx1
```
### kubectl create -f nginx-frontend.yaml
