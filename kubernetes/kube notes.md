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
#1 ETCD:
      etcd is a consistent and highly-available key value store used as Kubernetes’ backing store for all cluster data
      ETCD Stores information for nodes,pods,config,secret,accoutns,roles,bindings & others,
      every command u run through kubctl & every node added will be updated in etcd server
