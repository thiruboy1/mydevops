# Kubernetes
Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications.
## Kubernetes Cluster Archticture
      it mainly consist of 
            1) master node:
                  masternode consists of : 
                        #1 Kubeapi Server
                        #2 ETCD
                        #3 Controller Manager
                        #4 Kube Scheduler
            2) worker node
                        #1 kublet
                        #2 kube proxy
## 1 ETCD:
* Etcd is a consistent and highly-available key value store used as Kubernetes’ backing store for all cluster data
* ETCD Stores information for nodes,pods,config,secret,accoutns,roles,bindings & others, every command u run through kubctl & every node added will be updated in etcd server
* ETCD use port 2379
## KubeApi Server: 
* The Kubernetes API server validates and configures data for the api objects which include pods, services, replicationcontrollers, and others. The API Server services REST operations and provides the frontend to the cluster’s shared state through which all other components interact.
* kube api server performs following functions,
```
      * Authenticate user
      * validate request
      * retrive data
      * update etcd
      * scheduler
      * kubelet
 ```
* first it authentecate & validate user and retrives data from etcd and response back requested info, now schedluer contiounsly moniter the api server and identifys that no nodes is assigend for pod and then assigns node and communicate back to api server ,then api server updates back to etcd server, then api server sends to kubelet , then kubelet create appropriate pod in node and sends status to api server, then api server updates in etcd 
* kube api server file is located in /etc/kubernetes/manifests/kube-apiserver.yaml
* kube api services for nod kubeadmin setup  /etc/systemd/system/kube-apiserver.service
* ps -aux |grep kube-apiserver 
## Kube Controller Manager:
*   The Kubernetes controller manager is a daemon that embeds the core control loops shipped with Kubernetes. In applications of robotics and automation, a control loop is a non-terminating loop that regulates the state of the system. In Kubernetes, a controller is a control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state. Examples of controllers that ship with Kubernetes today are the replication controller, endpoints controller, namespace controller, and serviceaccounts controller
* kube controller manages nodes and pods , it moniters nodes and pods if anything it act accordingly 
* it consist of node controller ,replication controller, deployment controller,namespace controller, replicaset,pv controller ,endpoint controller,job controller, service account controller.
      ** node controller moniter nodes for every 5s
      ** it gives 40s to come back (grace period )
 * kube controller server file is located in /etc/kubernetes/manifests/kube-controller-manager.yaml
* kube api services for nod kubeadmin setup  /etc/systemd/system/kube-controller-manager.service 

## Kube Schedluer:
* The Kubernetes scheduler is a policy-rich, topology-aware, workload-specific function that significantly impacts availability, performance, and capacity. The scheduler needs to take into account individual and collective resource requirements, quality of service requirements, hardware/software/policy constraints, affinity and anti-affinity specifications, data locality, inter-workload interference, deadlines, and so on. Workload-specific requirements will be exposed through the API as necessary.

* scheduler decides which pods goes to which node , it decides based on requirments
first scheduler filter the node then scheduler ranks the node scale of 0 to 10, scheduer calculater amount resources free after placing pod, more free resources will get better rank

## kubelet:
* The kubelet is the primary “node agent” that runs on each node. The kubelet works in terms of a PodSpec. A PodSpec is a YAML or JSON object that describes a pod. The kubelet takes a set of PodSpecs that are provided through various mechanisms (primarily through the apiserver) and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn’t manage containers which were not created by Kubernetes.
Other than from a PodSpec from the apiserver, there are three ways that a container manifest can be provided to the Kubelet.
* File: Path passed as a flag on the command line. Files under this path will be monitored periodically for updates. The monitoring period is 20s by default and is configurable via a flag.

* HTTP endpoint: HTTP endpoint passed as a parameter on the command line. This endpoint is checked every 20 seconds (also configurable with a flag).

* HTTP server: The kubelet can also listen for HTTP and respond to a simple API (underspec’d currently) to submit a new manifest

## kube proxy:
  The Kubernetes network proxy runs on each node. This reflects services as defined in the Kubernetes API on each node and can do simple TCP, UDP, and SCTP stream forwarding or round robin TCP, UDP, and SCTP forwarding across a set of backends. Service cluster IPs and ports are currently found through Docker-links-compatible environment variables specifying ports opened by the service proxy. There is an optional addon that provides cluster DNS for these cluster IPs. The user must create a service with the apiserver API to configure the proxy.
  
## Pod:
 * pod is smallest object u can create in kubernetes
 * A Pod is the basic execution unit of a Kubernetes application–the smallest and simplest unit in the Kubernetes object model that you create or deploy. A Pod represents processes running on your Cluster .
 * Pods in a Kubernetes cluster can be used in two main ways:
      * Pods that run a single container
      * Pods that run multiple containers that need to work together
## Replication Controller:
* A ReplicationController ensures that a specified number of pod replicas are running at any one time. In other words, a ReplicationController makes sure that a pod or a homogeneous set of pods is always up and available
* another use of RC is during loadbalancing, if load increacese RC will replicate the pod is another node  in cluster when demand increces


## Replica Set
* main diffrence b/w replication controller and replication set is "selector", based on the label replicas is applied,
but if u have d
* A ReplicaSet’s purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often used to guarantee the availability of a specified number of identical Pods.However, a Deployment is a higher-level concept that manages ReplicaSets and provides declarative updates to Pods along with a lot of other useful features. Therefore, we recommend using Deployments instead of directly using ReplicaSets
### rc-set-defenation.yaml
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
* Replica Set can be updated by updating in rc-defination.yaml file and it can also be done using following command but note that updating throught command dosent update on yaml file
      * kubectl scale --replicas=6 -f replicaset defenation.yml
### Replica Set Commands
```
  kubectl create -f replication.yml
  kubectl get replicaset
  kubectl get rs
  kubectl get rs <rs name> -o yml                                   # you will get replicaset in yml file
  kubectl get pod db-1-7f6x2 -o yaml > db1.yaml
  kubectl delete replicaset myapp-replcation.yml
  kubectl replace -f replication.yml
  kubectl scale --replicas=6 -f replicaset defenation.yml         # Replica Set Scalling 
  kubectl edit replicaset <replicaset name>
```
# Deployments:
 * A Deployment controller provides declarative updates for Pods and ReplicaSets.

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
## Namespaces:
* Namespaces provide a scope for names. Names of resources need to be unique within a namespace, but not across namespaces. Namespaces can not be nested inside one another and each Kubernetes resource can only be in one namespace.
* Namespaces are a way to divide cluster resources between multiple users
* default namespace is created by kubernetes automaticlly when cluster is setup to  avoid deleting of resource kubernetes create another namespace called kube-system  and 3rd namespace created by kubernets is called kube-public
* u can also creat you own namespaces
* When you create a Service, it creates a corresponding DNS entry. This entry is of the form <service-name>.<namespace-name>.svc.cluster.local, which means that if a container just uses <service-name>, it will resolve to the service which is local to a namespace. This is useful for using the same configuration across multiple namespaces such as Development, Staging and Production. If you want to reach across namespaces, you need to use the fully qualified domain name
* if u want to create pod in ur namespace then u can use following command are u can specfiy in pod-definationfile.yaml under metadata 
      * kubectl create -f pod-definationi.yaml -n dev   # creates pod in custom(dev) namespaces
* creating namespace
```
      apiVersion: v1
      kind: Namespace
      metadata:
            name: dev
kubectl create -f file.yaml     
```
* to switch namespace form default namespace to custom (dev) namespace is by using following command
      * kubectl config set-context $(kubectl current-context) --namespace=dev
```
```
kubectl get namespaces
kubectl get pod --all-nampespaces
kubectl get pod -n kube-system
```
      
## Services:
* An abstract way to expose an application running on a set of Pods as a network service.
With Kubernetes you don’t need to modify your application to use an unfamiliar service discovery mechanism. Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them
* services enables to communicate b/w front and backend pods and helps in establsihing connectivity with external data sources

### node port serivce: 
      * listen on one of port and fordward request to pod on port running applicaiton, this type of service is know as node port serivce
```
![Image description](/images/service_nodeport.png)
```
### Cluster IP:
      * Service creates a virtual ip inside cluster to enable communcation b/w diffrent service such as set of forn end/backed servers
### Load Balancers:
      * to distribute load accros front end tier
      


































