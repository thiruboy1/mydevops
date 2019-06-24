# Kubernetes

Kubernetes Installation - https://github.com/thiruboy1/toolinstallation/blob/master/Kubernetes

## Kubernetes Guide

1. POD
2. Replication Controller & ReplicationSet:
    2.1 ReplicationController: will not have selctor
    
                apiVersion: v1
                kind: ReplicationController
                metadata:
                  name: nginx
                spec:
                  replicas: 3
                  selector:
                    app: nginx
                  template:
                    metadata:
                      name: nginx
                      labels:
                        app: nginx
                    spec:
                      containers:
                      - name: nginx
                        image: nginx
                        ports:
                        - containerPort: 80
    2.2. ReplicationSet Will have selector:Role of replication set is to monitor the pods and if any one fails it will run new pods, but how does this replication set will know which pod to monitor? 
    this is were we use lables and selectors,
     
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
3. Deployments
