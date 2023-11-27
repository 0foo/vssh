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


```
nick ~: vssh create 
Created connection: modest-haibt
Key generated: modest-haibt and modest-haibt.pub
Private Key location:/home/nick/.ssh/vssh/modest-haibt/modest-haibt
Public Key location: /home/nick/.ssh/vssh/modest-haibt/modest-haibt.pub
SSH Public key
----------------------------
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCVDXdTMWLxZL6eJXdjUb8oHMLFyTzI9wdnYRH/raXsxa7bCLEaS7ohQ+DR5eKfnJ7x4pQM43/Vxyj3/45kreCxZKmbLKzQEOidYvzBisa+8VieW2qxlseyVXCrB1YnAs/s+MkAEBehX2g5nxaqedseoqkh9pVi1hrnh5haWYCV6iANY7Yh9k0rPSZF6h2S8CygtpqHrWQq7u/p7uA6H+T3H0tguDV35F3gMcn0Qhy5f7ri4lVvIRUlRq7XQJPJzksFFpdEbO6sf/Gd4kqxKsM1zl9IEi9Wd/EdDWBZGv5zOOXtUD2ltDX8urRBCvhisgZITbsbdCCVxRbfcklgA4kH
nick ~/.nick_config_files/vssh (master) :
```
