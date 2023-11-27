# An simple SSH file creator
* use with an ssh-config manager to quickly create ssh keys
* combine with an ssh-config manager tool in order to have minimal pain setup of ssh connections
* this is the cryptography configuration
	* as of this writing it's:
		* public_exponent=65537
		* key_size=2048
	* https://github.com/0foo/nick_py_utils/blob/main/nick_py_utils/cryptography.py#L6
	* from what I've read these settings are sufficient for most normal people but a `to do` is to migrate the lib code into this repo add a config file to allow this to be configured
# Dependencies
* python on the system path 
    * verify by running /usr/bin/env python3


# To Use

```
        vssh <command> <optional connection name>

        vssh create [optional connection name]
		Created connection: modest-haibt
		Key generated: modest-haibt and modest-haibt.pub
		Private Key location:/home/nick/.ssh/vssh/modest-haibt/modest-haibt
		Public Key location: /home/nick/.ssh/vssh/modest-haibt/modest-haibt.pub
		SSH Public key
		----------------------------
		ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAs/s+MkAEBehX2g5nxaqedseoqkh9pVi1hrnh5h...........

        vssh list
            do-droplet-1
            jolly-haibt
            optimistic-wozniak
            aws-ec2-3kdf9

        vssh delete <connection name | all>
            Sucessfully deleted: elastic-hodgkin
```
