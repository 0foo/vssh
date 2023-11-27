# An simple SSH file creator
* use with an ssh-config manager to quickly create ssh keys
* combine with an ssh-config manager tool in order to have minimal pain setup of ssh connections

# Dependencies
* python on the system path 
    * verify by running /usr/bin/env python3


# To Use

```
        vssh <command> <connection> [options]

        vssh create [optional connection name]
            Created connection: optimistic-haibt
            Key Generated: optimistic-haibt and optimistic-haibt.pub
            SSH PUBLIC KEY
            ----------------------------
            ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCk5XpQuJc.....

        vssh list
            do-droplet-1
            jolly-haibt
            optimistic-wozniak
            aws-ec2-3kdf9

        vssh delete <connection name>
            Sucessfully deleted: elastic-hodgkin
```
