# Cluster Commands
      kubectl get services                # List all services 
      kubectl get pods                    # List all pods
      kubectl get nodes -w                # Watch nodes continuously
      kubectl version                     # Get version information
      kubectl cluster-info                # Get cluster information
      kubectl config view                 # Get the configuration
      kubectl describe node <node>        # Output information about a node

# Pod and Container
      kubectl get pods                         # List the current pods
      kubectl describe pod <name>              # Describe pod <name>
      kubectl get rc                           # List the replication controllers
      kubectl get rc --namespace="<namespace>" # List the replication controllers in <namespace> 
      kubectl describe rc <name>               # Describe replication controller <name> 
      kubectl get svc                          # List the services
      kubectl describe svc <name>              # Describe service <name>

# Interacting with Pods
      kubectl run <name> --image=<image-name>                             # Launch a pod called <name> 
                                                                          # using image <image-name>
      kubectl create -f <manifest.yaml>                                   # Create a service described 
                                                                          # in <manifest.yaml>
      kubectl scale --replicas=<count> rc <name>                          # Scale replication controller 
                                                                          # <name> to <count> instances
      kubectl expose rc <name> --port=<external> --target-port=<internal> # Map port <external> to 
                                                                          # port <internal> on replication 
     kubectl get nodes -o wide    # gets node ip address                                                                 
                                                                          
# ReplcationSet Commands
* A ReplicaSet’s purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often used to guarantee the availability of a specified number of identical Pods.However, a Deployment is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Therefore, we recommend using Deployments instead of directly using ReplicaSets
```
                        apiVersion: apps/v1
                        kind: ReplicaSet
                        metadata:
                          name: frontend
                          labels:
                            app: guestbook
                            tier: frontend
                        spec:
                          # modify replicas according to your case
                          replicas: 3
                          selector:
                            matchLabels:
                              tier: frontend
                          template:
                            metadata:
                              labels:
                                tier: frontend
                            spec:
                              containers:
                              - name: php-redis
                                image: gcr.io/google_samples/gb-frontend:v3
  ```
      kubectl create -f replication.yml
      kubectl get replicaset
      kubectl get rs
      kubectl get rs <rs name> -o yml                                   # you will get replicaset in yml file
      kubectl get pod db-1-7f6x2 -o yaml > db1.yaml
      kubectl delete replicaset myapp-replcation.yml
      kubectl replace -f replication.yml
      kubectl scale --replicas=6 -f replicaset defenation.yml
      kubectl edit replicaset <replicaset name>
                                                                    
# ReplcationController Commands
      kubectl create -f replicationController.yml
      kubectl get replicationcontroller
      kubectl delete replicationcontrollet myapp-replcation.yml
      kubectl replace -f replication.yml
# Kube Deployments Commands: 
* A Deployment controller provides declarative updates for Pods and ReplicaSets.
You describe a desired state in a Deployment, and the Deployment controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

```
      kubectl create -f deployment.yml
      kubectl get deployments
      kubectl get all
      kubectl rollout status deployment.v1.apps/nginx-deployment # to c deployment roll out status
      kubectl get pods --show-labels # to see labels 
```
```                       
                       apiVersion: apps/v1
                        kind: Deployment
                        metadata:
                          name: nginx-deployment
                          labels:
                            app: nginx
                        spec:
                          replicas: 3
                          selector:
                            matchLabels:
                              app: nginx
                          template:
                            metadata:
                              labels:
                                app: nginx
                            spec:
                              containers:
                              - name: nginx
                                image: nginx:1.7.9
                                ports:
                                - containerPort: 80
```
# Kube 

            kubectl run --generator=run-pod/v1 nginx-pod --image=nginx:alpine
            kubectl expose pod redis --port=6379 --name redis-service  #redis-service to expose the redis application within the cluster on port 6379
            kubectl create deployment webapp --image=kodekloud/webapp-color
            kubectl scale deployments/webapp --replicas=3
            kubectl expose deployment webapp --type=NodePort --port=8080 --name=webapp-service --dry-run -o yaml > webapp-service.yaml
                                                
# Kube Scheduling
It is responsible for placement of Pods on Nodes in a cluster.The scheduler finds feasible Nodes for a Pod and then runs a set of functions to score the feasible Nodes and picks a Node with the highest score among the feasible ones to run the Pod. The scheduler then notifies the API server about this decision in a process called “Binding

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
             nodeName: <node name>   # to get node name run <kubectl get node>
# Selecors and labels
      kubectl get pods --selector app=app1
      kubectl get all --selector env=prod
      kubectl get pods --selector bu=finance
      kubectl get all --selector env=prod,bu=finance,tier=frontend

                    apiVersion: apps/v1
                  kind: ReplicaSet
                  metadata:
                    name: replicaset-1
                  spec:
                    replicas: 2
                    selector:
                      matchLabels:
                        tier: frontend
                    template:
                      metadata:
                        labels:
                          tier: frontend
                      spec:
                        containers:
                        - name: nginx
                          image: nginx    
  
 # editing PODs and Deployments
            kubectl edit pod <pod name>
            kubectl edit deployment my-deployment
            kubectl get pods
            kubectl get pod -o yaml > lion.yaml
            edit lion.yaml file & delete lion poda and create lion pod usin lion.yaml file
            kubectl create -f lion.yaml 
                        
  # Daemone Sets
    Daemone set will make sure that service is running on all nodes
    A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Deleting a DaemonSet will clean up the Pods it created
  
            apiVersion: apps/v1
            kind: DaemonSet
            metadata:  
              name: elasticsearch
              namespace: kube-system
            spec:
              selector:
                matchLabels:
                  name: elasticsearch
              template:
                metadata:
                  labels:
                    name: elasticsearch
                spec:
                  containers:
                  - name: elasticsearch
                    image: k8s.gcr.io/fluentd-elasticsearch:1.20
                    
            master $ cat desets.yml
            
            apiVersion: apps/v1
            kind: DaemonSet
            metadata:
                name: elasticsearch
                namespace: kube-system
# Static Pods
           kublete is service installed in nodes , this kubelet can operate even without kube master, in order to run kubelet without master u need to place yaml file in /etc/kubernetes/manifestes/. now kublete will check for update in this location if any update kubelet will update the same in pod.
           in static pods you cannot create replica sets,deployments without kube master
           1) specfiy in kubelet.service file
           --pod-manifest-path=/etc/kubernetes/manifestes\\
           2)insted of defining in kubelet.service file create a kubeconfig.yaml and provide path in serive file and in that file enter the following
                  --config-kubeconfig.yaml
                  staticPodPath: /etc/kubernetes/manifestes
            kubectl get pods --all-namespaces
            kubectl run --restart=Never --image=busybox static-busybox --dry-run -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
            
# Kube Multiple Scheduler

* Kubernetes allows us to create multiple scheduler, in order to create custom scheduler u can use the schedule.yaml file in manifest folder, 
* you can have any number of custom scheduler, 
* in case of multiple scheduler , u must set leder elect to false in custom pod def file
* to create custom scheduler yaml file, juct copy the orginal scheduler file and update the custom name and create the scheduler 
* update "lock-object-name=my-custom-schuduler
* you can run pod with custome scheduler by inserting property in pod yaml file : schedulerName: my-custom-scheduler
            
                  apiVersion: v1
                  kind: Pod
                  metadata:
                    name: nginx
                  spec:
                    containers:
                    -  image: nginx
                       name: nginx
                    schedulerName: my-scheduler
* to check which scheduler created pod use following command.
kubctl get events

# Kube Monitoring & loging
            Kubernetes dosent have complete monitoring feature, so we use other tools like metrics
            metrics installatino:
            https://github.com/kodekloudhub/kubernetes-metrics-server.git
            cd <downloded folder>
            kubectl creat -f .
            kubectl top nodes
            kubectl top pods
      ## Log
            simalar like docker kubernetes have feature to moniter logs, by using simple command,
            kubernets allows us to moniter multiple contianers in single pod by using following command
            kubectl log -f <pod name> <container name>
# Kube Application lifecycle Managment
            in kubernetes there two types of update are there
            1)Rolling Update(Default): 
                in this kuberenetes will bring up new pod and bring down old pod, by this way it will roll all the pods, 
                if there is any issue in new updated pod then u can roll back to old pods
            2)Recreate Update:
              old pods are Destroyed and new pods are created, in this method there will application down time
              
              kubectl create -f deployment-defination.yaml                    #create
              kubectl get deployments                                         #get
              kubectl describe deployment
              kubectl apply -f deployment-defination.yaml                     #update
              kubectl set image deployment/myapp-deployment nginx=nginx:1.9.1
              kubectl rollout status deployment/myapp-deployment              #status
              kubectl rollout history                                         #rollback
              
# Kube Env Variables
              in pod defination file u can specfiy the env variables, Enfiroment variable can be set in two ways
         ## 1) direct way
             
              to set an Enviorment variable use "env" array
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
            
      when you have lot pods it will become difficult to manage Envirorment Variables so we use config map                
              
      ## 2)Config Maps:
             is used to pass configuration data in the form of key value pairs in kubernetes
             there are two phases in config map 1) create config map file 2) inject into kubernetes
             imperative  way: kubectl create configmap
                                    <config-name> --from-literal=<key>=<value>
                                                  --from-literal=<key>=<value>
                                                  --from-literal=<key>=<value>
                              kubectl create configmap
                                    <config-name> --from-file=<path to file>
                                    
             declarative way: kubectl create -f configmap.yaml 
             
                              apiVersion: v1
                              kind: ConfigMap
                              metadata:
                                  name: app-config
                              data:
                                 APP_COLOR: pink
                                 APP_MODE: prod
              
            kubectl get configmaps
            kubectl describe configmaps
            
      ## now inject configmap file into pod defination file
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
            
# Kube Secrets
       kubernetes allows us to store user name password in more secure way by using secrets, you can define secretes in 2 ways
       2)imperative way 2)declarative way
       imperative  way: kubectl create secret
                                    <secret-name> --from-literal=<key>=<value>
                                                  --from-literal=<key>=<value>
                                                  --from-literal=<key>=<value>
                              kubectl create secret
                                    <secret-name> --from-file=<path to file>
                                    
             declarative way: kubectl create -f secret.yaml 
             
                              apiVersion: v1
                              kind: Secret
                              metadata:
                                  name: app-secret
                              data:
                                 db_host: 
                                 db_username
                                 db_password: 
            
            to generate hash version of db host and db_password use following command in linux 
            echo -n 'mysql' | base64
            echo -n 'root' | base64
            echo -n 'pass' | base64
            kubectl get configmaps
            kubectl describe configmaps
## now inject secret file into pod defination file
      appVersion: v1
              kind: Pod
              metadata:
                  name: testpod
              spec:
                  container:
                    - name:
                      image:
                      envFrom:
                        - secretRef:
                               name: app-secret(name of config map which was created)           
 ## secret in POD as volume
            volume:
             - name: app-secret-volume
               secret:
                 secretName: app-secret       
            
# Kube Mulit Container Pod     
# kube initContainer
            init container will run before app container will start run,
            If an Init Container fails for a Pod, Kubernetes restarts the Pod repeatedly until the Init Container succeeds,However, if the Pod has a restartPolicy of Never, it is not restarted .
            apiVersion: v1
            kind: Pod
            metadata:
              name: myapp-pod
              labels:
                app: myapp
            spec:
              containers:
              - name: myapp-container
                image: busybox:1.28
                command: ['sh', '-c', 'echo The app is running! && sleep 3600']
              initContainers:
              - name: init-myservice
                image: busybox:1.28
                command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
# Kube OS upgrade to node
             in kube cluster if any node need to updated then node needs downtime, during this down time pods will also go down,
             eviction timeout 5 m, the time it waits for pod to come back is called eviction timeout, which is set on controller manager
             with default value of 5 miniutes.so when ever node goes down,master node waits for 5m to consedring node dead.
             if node comes back after eviction time then node comes blank.
             so if u have any maintince task to be performed then u drain the node by running following command
            # kubectl drain node-1
             once maintanence activity is done u need to run following command so that master will assign pods to node
            # kubectl uncordon node-1
            # kubectl cordon   # this command will not terminate insted it will make sure that new pods should not be scheduled
              kubectl get pods -o wide
              
              Upgrade of cluster: all components of kubernetes must be one version lower than kubeapiserver, kubectl can be one version lower or upper, ant any time kubernetes will to use 3 stable version,
              1st u need to upgrage kube master and then u need to updgarde nodes , during master upgrade nodes will work independtly, users will not have any intruption but master cannot control nodes
              apt install kubeadm=1.12.0-00
              kubeadm upgrade apply v1.12.0
              apt install kubelet=1.12.0-00            
# Backup and restore methods
# Kube Security
# Kube Storage
          volumes
          persistant Volumes
          Persistant Volume claims
# namespace Network
      ip link    # display host interface
      ip netns add <pod>
      ip netns
      ip netns exec <pod> ip link
      ip -n <pod> ip link
      ip netsn exec <pod> apr
      --------------------link two pod red and blue run following command
      ip link add veth-red type veth peer name veth-blue # to add two nampspace network use pipe like connecting two pc using cable
      ip link set veth-red netns red # attaching virtual interface to pod
      ip link set veth-blue netns blue # attaching virtual interface to pod
      ip -n red addr add <ip> dev veth-red
      ip -n blue addr add <ip> dev veth-blue # now both pods can communicate each other
      --------when number of pod increases then in order to establish communication b/w all pods u need n/w bridge-------
      linux bridge:
      ip link add v-net-0 type bridge
      ip link set dev v-net-0 up # to bring it up
      ip link add veth-red type veth peer name veth-red-br # creates cable to connect red pod to bridge n/w
      ip link add veth-blue type veth peer name veth-blue-br # creates cable to connect red pod to bridge n/w
      ip link set veth-red netns red  
      ip link set veth-red-br master v-net-o
      ip link set veth-blue netns blue
      ip link set veth-blue-br master v-net-o
      ip -n red addr add <ip> dev veth-red
      ip -n red addr add <ip> dev veth-red
      -----------------lab workouts history
                        kubectl get nodes
                      8  ip netns
                      9  ip link
                     10  kubectl get nodes -o wide
                     11  kubectl describe node master
                     12  ip link show ens3
                     13  kubectl get nodes -o wide
                     14  arp node02
                     15  arp node01
                     16  arp master
                     17  ip link
                     18  ip route show default
                     19  netstat -nplt
     --------------------------------------------------------------------------------------------------------
     # to check ip range configured for service within in cluster
        ps -aux | grep kube-api
     #  To check ip range of pod 
        kubectl logs weave-net-dhrx8   weave -n kube-system
     # To check how kube proxy is controlled to run on service
        kubectl describe pod <kube-proxy> -n kube-system # see controlled by
          
          
   # DNS in Kubernetes
      # Core DNS :
           kubernetes deployes coredns pods(in replicat set for redundancy) on cluster to resolve the pods,
           all pod ip and name details are moved to central dns server (core dns) then when pods want to communicate to other pod it checks coredns records and identifys pod and establish connection.
           when coredns is created , master will create a services "kube-dns" 'kubectl get service kube-dns -n kube-system' 
           kubelet service is responsiable for this  'cat /var/lib/kubelet/config.yaml'
           when pod is created, pod dns server detials is entered in /etc/resolv.conf file . so by this way pod will check the coredns entry 
           in order to edit Corefile u can edit configmap 'kubectl edit configmap -n kube-system'
       core dns requries a config file which is placed in /etc/coredns/Corefile in this file plugins are configured
       kubectl get service -n kube-system        # To check kube dns details
       kubectl exec <core-dns-pod-name> -n kube-system ps   # Where is the configuration file located for configuring the CoreDNS service?
       core dns file is configured to dns pod using configmap
       kubectl get configmap -n kube-system
       kubectl describe configmap coredns -n kube-system
# Ingress
      Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource
      An Ingress can be configured to give Services externally-reachable URLs, load balance traffic, terminate SSL / TLS, and offer name based virtual hosting
      You must have an ingress controller to satisfy an Ingress. Only creating an Ingress resource has no effect
      Ingress needs 
                  1) ingress controller(suppotrs gcp,ngnix)
                        a) service to expose node port to external wo
                        b) service account to write correct permission- cluster roles role bingings
                        c) config map to feed nginx data 
                  2) ingress resources (.yaml file)
      
   1) ingress controller: its deployed as normal pod deployment 
   '''
   ---------------------code.yaml-------------------------------------
                                          apiVersion: extensions/v1beta1
                                          kind: Ingress
                                          metadata:
                                            name: ngnix-ingress-controller
                                          spec:
                                           replicas: 1
                                           selector: 
                                              matchLabels:
                                                  name: ngnix-ingress
                                           tempelate:
                                              metadata:
                                                 labels: 
                                                   name: ngnix-ingress
                                              spec:
                                                containers:
                                                - name:
                                                  image:
-------------------------------------------------------------------
                  
            2)ingress resources:
                        apiVersion: networking.k8s.io/v1beta1
                        kind: Ingress
                        metadata:
                          name: test-ingress
                          annotations:
                            nginx.ingress.kubernetes.io/rewrite-target: /
                        spec:
                          rules:
                          - http:
                              paths:
                              - path: /testpath
                                backend:
                                  serviceName: test
                                  servicePort: 80
          
     4  kubectl get deployments --all-namespaces
    5  kubectl create namespace ingress-space
    6  kubectl get namespace
    7  kubectl create configmap nginx-configuration -n ingress-space
    8  kubectl get configmap -n ingress-space
    9  kubectl create searviceaccount ingress-serviceaccount -n ingress-space
   10  kubectl create serviceaccount ingress-serviceaccount -n ingress-space
   11  kubectl get serviceaccount -n ingress-space
   12  kubectl get roles -n ingress-space
   13  kubectl get rolebinding -n ingress-space         
          
          
          
