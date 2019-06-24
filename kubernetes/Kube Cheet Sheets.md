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
                                                                          # controller <name>
# ReplcationSet Commands
      kubectl create -f replication.yml
      kubectl get replicset
      kubectl delete replicaset myapp-replcation.yml
      kubectl replace -f replication.yml
      kubectl scale -replicas=6 -f replicaset defenation.yml
                                                                    
# ReplcationController Commands
      kubectl create -f replicationController.yml
      kubectl get replicationcontroller
      kubectl delete replicationcontrollet myapp-replcation.yml
      kubectl replace -f replication.yml
                                                
