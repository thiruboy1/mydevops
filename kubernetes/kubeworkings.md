
## kubectl get nodes --show-labels


## make a note of manual scheduling pod to node
## taints and tolerations
## make note of nodeselectors
## make a note of nodeaffinity





```

```

```
      add nodeName in yaml file 
      apiVersion: v1
      kind: pod
      metadata: 
          name: nginx
          labels:nginx-app
      spec:
         containers: 
         -  image: nginx
            name: nginx
         nodeName: <node name> 
```

```
kubectl taint nodes node1 key1=value1:NoSchedule
kubectl taint nodes node1 key1=value1:NoExecute
kubectl taint nodes node1 key2=value2:NoSchedule
```


```
  tolerations:
  - key: "spray"
    operator: "Equal"
    value: "mortein"
    effect: "NoSchedule"
```


```
 apiVersion: v1
kind: Pod
metadata:
 name: nginx
 labels:
   env: test
spec:
 containers:
 - name: nginx
   image: nginx
   imagePullPolicy: IfNotPresent
 nodeSelector:
   size: large   
```


```
     affinity:
       nodeAffinity:
         requiredDuringSchedulingIgnoredDuringExecution:
           nodeSelectorTerms:
           - matchExpressions:
             - key: node-role.kubernetes.io/master
               operator: Exists
```
```
apiVersion: v1
kind: LimitRange
metadata:
  name: mem-limit-range
spec:
  limits:
  - default:
      memory: 512Mi
    defaultRequest:
      memory: 256Mi
    type: Container
```

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: mem-cpu-demo
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi
```

* Create a static pod named static-busybox that uses the busybox image and the command sleep 1000
```
            kubectl run --restart=Never --image=busybox static-busybox --dry-run -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
 ```
### custom scheduler in pod defination file
```
                 apiVersion: v1
                 kind: Pod
                 metadata:
                   name: nginx
                 spec:
                   containers:
                   -  image: nginx
                      name: nginx
                   schedulerName: my-scheduler
```

```
          appVersion: v1
          kind: Pod
          metadata:
              name: testpod
          spec:
              container:
                - name:
                  image:
             env:
              - name: APP_Color
                value: pink
```

```
 imperative  way: kubectl create configmap
                                <config-name> --from-literal=<key>=<value>
                                              --from-literal=<key>=<value>
                                              --from-literal=<key>=<value>
                          kubectl create configmap
                                <config-name> --from-file=<path to file>
```

```
now inject configmap file into pod defination file
  appVersion: v1
          kind: Pod
          metadata:
              name: testpod
          spec:
              container:
                - name:
                  image:
                  envFrom:
                  - configMapRef:
                     name: app-config(name of config map which was created)
                    
```
## Backup and restore

 ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /tmp/snapshot-pre-boot.db. 
 
 ## Restore
 
 ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --name=master \
     --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key \
     --data-dir /var/lib/etcd-from-backup \
     --initial-cluster=master=https://127.0.0.1:2380 \
     --initial-cluster-token=etcd-cluster-1 \
     --initial-advertise-peer-urls=https://127.0.0.1:2380 \
     snapshot restore /tmp/snapshot-pre-boot.db
     
  ## Modify /etc/kubernetes/manifests/etcd.yaml
  
  Update --data-dir
  ```
  --data-dir=/var/lib/etcd-from-backup
  ```
 Update new initial-cluster-token to specify new cluster
 ```
 --initial-cluster-token=etcd-cluster-1
 ```
 Update volumes and volume mounts to point to new path
```
    volumeMounts:
    - mountPath: /var/lib/etcd-from-backup
      name: etcd-data
    - mountPath: /etc/kubernetes/pki/etcd
      name: etcd-certs
  hostNetwork: true
  priorityClassName: system-cluster-critical
  volumes:
  - hostPath:
      path: /var/lib/etcd-from-backup
      type: DirectoryOrCreate
    name: etcd-data
  - hostPath:
      path: /etc/kubernetes/pki/etcd
      type: DirectoryOrCreate
    name: etcd-certs
 ```

# Kubernetes Certificates

```

{
#ca
echo "Creating CA Certificate"
openssl genrsa -out ca.key 2048
openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr
openssl x509 -req -in ca.csr -signkey ca.key -CAcreateserial -out ca.crt -days 1000

#admin
echo "Creating admin Certificate"
openssl genrsa -out admin.key 2048
openssl req -new -key admin.key -subj "/CN=KUBE-ADMIN/O=SYSTEM.MASTERS" -out admin.csr
openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out admin.crt -days 1000

#kube-schduler
echo "Creating Scheduler Certificate"
openssl genrsa -out sch.key 2048
openssl req -new -key sch.key -subj "/CN=SYSTEM-KUBE-SCH" -out sch.csr
openssl x509 -req -in sch.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out sch.crt -days 1000

echo "Creating Controller Certificate"
#kube-controller
openssl genrsa -out cont.key 2048
openssl req -new -key cont.key -subj "/CN=SYSTEM-KUBE-CONT" -out cont.csr
openssl x509 -req -in cont.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out cont.crt -days 1000

#kube proxy
echo "Creating proxy Certificate"
openssl genrsa -out proxy.key 2048
openssl req -new -key proxy.key -subj "/CN=SYSTEM-KUBE-PROXY" -out proxy.csr
openssl x509 -req -in proxy.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out proxy.crt -days 1000


#kubeapiserver
echo "Creating Server Config CNF File Certificate"
cat >server-config.cnf<<EOF
[ req ]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[ req_distinguished_name ]
[ v3_req ]
basicConstraints=CA:FALSE
keyUsage=nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage=serverAuth,clientAuth
subjectAltName=@alt_names
[ alt_names ]
DNS.1 = kubernetes
DNS.2 = kubernetes.default
DNS.3 = kubernetes.default.svc
DNS.4 = kubernetes.default.svc.cluster
DNS.5 = kubernetes.default.svc.cluster.local
IP.1 = 10.200.20.247
EOF
echo "Creating server Certificate"
openssl genrsa -out server.key 2048
openssl req -new -key server.key -subj "/CN=KUBE-SERVER" -out server.csr -config server-config.cnf
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -extensions v3_req -extfile server-config.cnf -out server.crt -days 1000




#etcd server
echo "Creating etcd config cnf file"

cat >etcd-config.cnf<<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
IP.1 = 10.200.20.247
IP.2 = 127.0.0.1
EOF

echo "Creating etcd server Certificate"
echo "Creating etcd Certificate"

openssl genrsa -out etcd.key 2048
openssl req -new -key etcd.key -subj "/CN=KUBE-ETCD" -out etcd.csr -config etcd-config.cnf
openssl x509 -req -in etcd.csr -CA ca.crt -CAkey ca.key -CAcreateserial -extensions v3_req -extfile etcd-config.cnf -out etcd.crt -days 1000

# etcdpeer
echo "Creating etcd peer Certificate"
openssl genrsa -out etcdpeer.key 2048
openssl req -new -key etcdpeer.key -subj "/CN=KUBE-ETCDPEER" -out etcdpeer.csr 
openssl x509 -req -in etcdpeer.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out etcdpeer.crt

#service account
echo "Creating service accoount Certificate"
openssl genrsa -out service-account.key 2048
openssl req -new -key service-account.key -subj "/CN=service-accounts" -out service-account.csr
openssl x509 -req -in service-account.csr -CA ca.crt -CAkey ca.key -CAcreateserial  -out service-account.crt -days 1000

#worker-1
echo "Creating worker Certificate"
cat >worker1-config.cnf<<EOF
[ req ]
req_extensions = v3_ext
distinguished_name = req_distinguished_name

[ req_distinguished_name ]
[ v3_ext ]
basicConstraints=CA:FALSE
keyUsage=keyEncipherment,dataEncipherment
subjectAltName=@alt_names
[ alt_names ]
IP.1 = 10.200.20.248

EOF

openssl genrsa -out worker1.key 2048
openssl req -new -key worker1.key -subj "/CN=system:node:worker1/O=systems:nodes" -out worker1.csr -config worker1-config.cnf
openssl x509 -req -in worker1.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out worker1.crt -extensions v3_ext -extfile worker1-config.cnf
}



```




