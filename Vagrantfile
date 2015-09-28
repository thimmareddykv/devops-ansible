#m -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  #config.vm.box = "deb/jessie-amd64"
  #config.vm.box_url = "https://github.com/holms/vagrant-jessie-box/releases/download/Jessie-v0.1/Debian-jessie-amd64-netboot.box"
  config.vm.hostname = "debian-vagrant"
  config.vm.network :private_network, ip: "192.168.50.50"
#  config.vm.network "public_network", bridge: 'eth0'
config.vm.network "public_network", ip: '192.168.s.220', bridge: 'eth0'
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "vagrant-provision.yaml"
    ansible.inventory_path = "hosts/vagrant.ini"
    ansible.host_key_checking = "false"
    ansible.limit = "all"
  end
  config.vm.provider :virtualbox do |vb|
    #vb.gui = true
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end
#  config.vm.synced_folder ".", "/vagrant", owner:"www-data", group:"www-data", mount_options:["dmode=775", "fmode=775"]
end
