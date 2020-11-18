#!/bin/bash
echo "************************* Yum update  *********************************************************************"
sudo yum -y update
echo "************************* Installing docker ***************************************************************"
sudo amazon-linux-extras install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user


echo "************************* Kubernetes pre settings *********************************************************"
sudo cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sudo sysctl --system


sudo cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kubelet kubeadm kubectl
EOF

sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
sudo systemctl enable --now kubelet
sudo systemctl daemon-reload
sudo systemctl restart kubelet

echo "***************************** Python Installation ******************************************************"
sudo amazon-linux-extras install -y python3
sudo curl -O https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py --user
sudo rm -rf /usr/bin/python
sudo  ln -s python3.6 python
sudo pip3.6 install --upgrade pip
sudo pip3.6 install openshift --user


echo "***************************** Ansible Installation ******************************************************"
sudo amazon-linux-extras install ansible2

echo "***************************** kube init ******************************************************"
kubeadm init --ignore-preflight-errors all

echo "************************* Creting kube token  *************************************************************"
sudo sleep 1
sudo kubeadm token create --print-join-command > /var/kubeadm-join

echo "************************* Creting Kube Config Files  *******************************************************"
sudo sleep 2
sudo mkdir -p $HOME/.kube
sudo sleep 5
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo sleep 5
sudo chown $(id -u):$(id -g) $HOME/.kube/config

echo "************************* Creting ssh keys  ***************************************************************"
sudo mkdir /home/ec2-user/.ssh
sudo cd .ssh
sudo yes id_rsa | ssh-keygen -q -t rsa -N '' >/dev/null


sudo hostnamectl set-hostname k8master.com
sudo kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"
