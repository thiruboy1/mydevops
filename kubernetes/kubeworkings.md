
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
