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
            * Authenticate user
            * validate request
            * retrive data
            * update etcd
            * scheduler
            * kubelet
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


