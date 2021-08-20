# An SSH manager


# Dependencies
* docker installed and working
    * verify by running `docker` on the command line 

* python on the system path 
    * verify by running /usr/bin/env python3

# Setup
1. clone the repo 
2. add bin directory to path
3. vssh-init
    * will build the docker image


* To use:

```
     vssh <command> <connection> [options]

        vssh create [optional connection name]
            Creating optimistic-haibt
            Key Generated: key and key.pub
            SSH PUBLIC KEY
            --------------------
            ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCk5XpQuJc.....


        vssh list
            vssh managed ssh connections
            --------------
            do-droplet-1 : user=ubuntu host=127.0.0.1 port=22 note="test me out"
            jolly-haibt : user=root host=137.229.3.12 port=22 note="my DO droplet"
            optimistic-wozniak : user=root host=127.0.0.1 port=22 note="local testing"
            aws-ec2-3kdf9 : user=ubuntu host=122.2.34.15 port=22 note="work ec2 instance"


        vssh delete jolly-haibt
            Deleted jolly-haibt


        vssh edit optimistic-wozniak -n "edited note" -h 1.1.1.1 -u test_user
        
        
        vssh list
            vssh managed ssh connections
            --------------
            do-droplet-1 : user=ubuntu host=127.0.0.1 port=22 note="test me out"
            optimistic-wozniak : user=test_user host=1.1.1.1 port=22 note="edited note"
            aws-ec2-3kdf9 : user=ubuntu host=122.2.34.15 port=22 note="work ec2 instance"
        

        vssh optimistic-wozniak
            Last login: Mon Aug 16 23:56:04 2021 from 170.12.12.148
            root@ubuntu-s-2vcpu-4gb-amd-sfo3-01:~#

```


# Notes
* All of the keys and config are stored in .ssh directory on the local machine under the folder of the machine name



# to do
* cli autocomplete
* vssh backup/restore
    * put all of the vpass managed folders and optionally ALL keys in .ssh into an encrypted compressed file
