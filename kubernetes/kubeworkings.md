
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

