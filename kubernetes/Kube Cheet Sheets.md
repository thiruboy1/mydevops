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
# Kube Deployments Commands
      kubectl create -f deployment.yml
      kubectl get deployments
      kubectl get all
# Kube 

            kubectl run --generator=run-pod/v1 nginx-pod --image=nginx:alpine
            kubectl expose pod redis --port=6379 --name redis-service  #redis-service to expose the redis application within the cluster on port 6379
            kubectl create deployment webapp --image=kodekloud/webapp-color
            kubectl scale deployments/webapp --replicas=3
            kubectl expose deployment webapp --type=NodePort --port=8080 --name=webapp-service --dry-run -o yaml > webapp-service.yaml
                                                
# Kube Scheduling
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
  
            apiVersion: apps/v1
            kind: DaemonSetmetadata:  name: elasticsearch
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
           2)insted of defining in kubelet.service file provide path in serive file and in that file enter the following
                  --config-kubeconfig.yaml
                  staticPodPath: /etc/kubernetes/manifestes
            kubectl get pods --all-namespaces
            kubectl run --restart=Never --image=busybox static-busybox --dry-run -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
            
# Kube Multiple Scheduler

Kubernetes allows us to create multiple scheduler, in order to create custom scheduler u can use the schedule.yaml file in manifest folder, 
you can have any number of custom scheduler, 
you can run pod with custome schedulet by inserting propert in pod yaml file : schedulerName: my-custom-scheduler
            
                  apiVersion: v1
                  kind: Pod
                  metadata:
                    name: nginx
                  spec:
                    containers:
                    -  image: nginx
                       name: nginx
                    schedulerName: my-scheduler
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
            
            
            
            
            
            
            
