## 1)create vpc,subnet,routetable,igw,ec2, with following tags
```
kubernetes.io/cluster/kuberntes 	owned
```
## 2) install kubeadm kubelet ..etc
## 3) mention --cloud-provider=aws in /var/lib/kubelet/kubeadm.env file on all servers
## 2)create aws.yaml file --cloud-provider=aws
```
---
apiVersion: kubeadm.k8s.io/v1beta2
kind: ClusterConfiguration
networking:
  serviceSubnet: "10.100.0.0/16"
  podSubnet: "10.244.0.0/16"
apiServer:
  extraArgs:
    cloud-provider: "aws"
controllerManager:
  extraArgs:
    cloud-provider: "aws"
```
## 3)create storage class-gp2

```
apiVersion: storage.k8s.io/v1beta1
kind: StorageClass
metadata:
  name: gp2
  annotations:
    storageclass.beta.kubernetes.io/is-default-class: "true"
  labels:
    kubernetes.io/cluster-service: "true"
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
```  

## 4)create pv:
```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-static
spec:
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: failure-domain.beta.kubernetes.io/zone
          operator: In
          values:
          - ap-south-1a
  capacity:
    storage: 8Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: gp2
  awsElasticBlockStore:
    fsType: ext4
    volumeID: vol-079de81078f84937e
    
```    
## 5)create pvc:
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvc-static
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
  volumeName: pv-static
```

## 7)create pod
```
apiVersion: v1
kind: Pod
metadata:
  name: pv-static-pod
spec:
  volumes:
    - name: pv-static-storage
      persistentVolumeClaim:
        claimName: pvc-static
  containers:
    - name: pv-static-container
      image: nginx
      ports:
        - containerPort: 80
          name: "nginx"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: pv-static-storage
```
-----------------------------------------------------------------------

## dynamic pv
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvc-dynamic
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi

```
## create pod:
```
apiVersion: v1
kind: Pod
metadata:
  name: pv-dynamic-pod
spec:
  volumes:
    - name: pv-dynamic-storage
      persistentVolumeClaim:
        claimName: pvc-dynamic
  containers:
    - name: pv-dynamic-container
      image: nginx
      ports:
        - containerPort: 80
          name: "nginx"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: pv-dynamic-storage
```
