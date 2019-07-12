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


