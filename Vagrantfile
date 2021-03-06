# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.define "project1" do |config|
    config.vm.box = "bento/ubuntu-20.04"
    config.vm.hostname = "node1"
    config.vm.box_check_update = false
    config.vm.network "private_network", ip: "10.0.7.10"
    config.vm.provision "shell", inline: <<-SHELL

      # Docker
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
      
      # Docker Compose
      sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      sudo chmod +x /usr/local/bin/docker-compose

      # up
      docker build -t project1/php /vagrant/php/;
      docker build -t project1/python /vagrant/python/;
      docker-compose up -d;

    SHELL

    config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end



end
