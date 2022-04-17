# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"

  # Accessing "localhost:< host port>" connect to VM "guest port"
  # NOTE: This will enable public access to the opened port
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # This is how to give name to machines
  config.vm.define :pythontest do |pythontest_config|  # this names it for vagrant
    pythontest_config.vm.hostname = "pythontest"
    pythontest_config.vm.provider "virtualbox" do |v|
      v.name = "pythontest"   # this names it for oracle gui 
    end
  end

  # We install for tests
  config.vm.provision "shell", inline: <<-SHELL
    su -l vagrant -c 'echo "set bell-style none" > /home/vagrant/.inputrc'
    apt-get -q update
    apt-get -qq upgrade
    apt-get -qq install git python3.8 python3-pip python3.8-venv
    python3 --version
    pip3 --version
  SHELL
end
