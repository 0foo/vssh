# An SSH manager


# Dependencies
* docker installed and working
    * verify by running `docker` on the command line 

# Setup
1. clone the repo 
2. add bin directory to path
3. vpass-init
    * will build the docker image


* To use:

```
    vpass <command> <machine> [options]

    vssh create
        Creating /data/optimistic-haibt
        Key Generated: key and key.pub
        SSH PUBLIC KEY
        --------------------
        ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCk5XpQuJcYvoXiaBsc9/vFoibqcpR9GrISk9HWwRhmUAg2MLrHNbMskHj4b/A0RCLzQW/GEB08oAR7ArUu9Uwn1anOmLQbXFaCTCsI8rfO4XBrFluU+FGm7VQQUyaN+jjiJcShR4m3lzRPLuqZNJb/D+DQjT446rnlAKlTMj1DGApgMyOXWo9dvpNXYWlQNagARu5RvgK2JAkoSXCYxYHmsa06XtT3PvIMYh+xUrh6EWmk+rYN7qqxJe8woI9+XZ4q7MYBdk+Wd+QvZ0lJlfsA3HCHJpgrdugPtL+U+P9TFp/S6A41fWOmatN7yls73heWEzkhEgMQQmdIKi0wqSMflam4OAJUvT6AG6yUiHfFj43Q340iLfc1YyyuwDAAfpCS0DR7G+LqddyNbEoUS0Lhhf29ClKb7crJTwhhQT4nbch9Lzucfk1b0eB2pkoD6nrx+JZJv14vQgJIgMtg7Mm4FB2CwPTHQfyYKxrYqni6E98R7NvfyiNwNkuzDmiM1cVi9GtQCOaDhwRfRxzkFjeXVgI/ApknhALmFlfr1mV+3SGVc1OnFSmOsksdV7OFKaRHZF3Xm8ZDiEVTXQ30fh6zWJTwNeUafkabBm/jNqgDiXYIGo/Bl7ApTfvYWbaVMY03A50IwuFLfjczl9qJ0uIziNp4JT08YmJ2amN2lU3AwQ== root@3ffaed78db38

    vssh optimistic-haibt
        ssh -o StrictHostKeyChecking=no -i /data/optimistic-haibt/key root@137.184.5.164
        Warning: Permanently added '137.184.5.164' (ECDSA) to the list of known hosts.
        Welcome to Ubuntu 21.04 (GNU/Linux 5.11.0-18-generic x86_64)

        * Documentation:  https://help.ubuntu.com
        * Management:     https://landscape.canonical.com
        * Support:        https://ubuntu.com/advantage

        System information as of Tue Aug 17 00:04:18 UTC 2021

        System load:  0.05              Users logged in:       0
        Usage of /:   1.9% of 77.36GB   IPv4 address for eth0: 137.184.5.164
        Memory usage: 4%                IPv4 address for eth0: 10.48.0.5
        Swap usage:   0%                IPv4 address for eth1: 10.124.0.2
        Processes:    103

        1 update can be applied immediately.
        To see these additional updates run: apt list --upgradable


        Last login: Mon Aug 16 23:56:04 2021 from 174.203.65.152
        root@ubuntu-s-2vcpu-4gb-amd-sfo3-01:~#

    vssh delete optimistic-haibt
        Deleted optimistic-haibt


```


# Notes
* All of the keys and config are stored in .ssh directory on the local machine under the folder of the machine name



# to do
* cli autocomplete
* vssh backup/restore
    * put all of the vpass managed folders and optionally ALL keys in .ssh into an encrypted compressed file
