# -*- mode: ruby -*-
# vi: set ft=ruby :

# install Docker
$setup_docker = <<SCRIPT
sudo apt update;
sudo apt full-upgrade -y;
sudo apt-get remove docker docker-engine docker.io containerd runc;
sudo apt-get install ca-certificates;
sudo apt-get install curl;
sudo apt-get install gnupg;
sudo apt-get install lsb-release;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg;
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null;
sudo apt update;
sudo apt-get install docker-ce docker-ce-cli containerd.io -y;

sudo usermod -aG docker vagrant;
SCRIPT

# create nodes
Vagrant.configure("2") do |config|

  config.vm.define "node1" do |config|
    config.vm.box = "bento/ubuntu-20.04"
    config.vm.hostname = "node1"
    config.vm.box_check_update = false
    config.vm.network "private_network", ip: "10.0.7.10"
    config.vm.provision "shell", inline: $setup_docker
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end

  #config.vm.define "node2" do |config|
  #  config.vm.box = "bento/ubuntu-20.04"
  #  config.vm.hostname = "node2"
  #  config.vm.box_check_update = false
  #  config.vm.network "private_network", ip: "10.0.7.11"
  #  config.vm.provision "shell", inline: $setup_docker
  #  config.vm.provider "virtualbox" do |vb|
  #    vb.memory = "2048"
  #  end
  #end

  #config.vm.define "node3" do |config|
  #  config.vm.box = "bento/ubuntu-20.04"
  #  config.vm.hostname = "node3"
  #  config.vm.box_check_update = false
  #  config.vm.network "private_network", ip: "10.0.7.12"
  #  config.vm.provision "shell", inline: $setup_docker
  #  config.vm.provider "virtualbox" do |vb|
  #    vb.memory = "2048"
  #  end
  #end

end
