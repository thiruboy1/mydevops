
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






