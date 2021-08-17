import os, argparse, shutil, yaml, shutil
from yaml.loader import SafeLoader
import random_names
from pathlib import Path

# pars args
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("command", type=str, nargs='?', default=None)
parser.add_argument("ssh_connection_name", type=str, nargs='?', default=None)
parser.add_argument("-p", "-port", type=int, default=None)
parser.add_argument("-u", "-user", type=str, default=None)
parser.add_argument("-h", "-host", type=str, default=None)

args = parser.parse_args()

# arguments
command=args.command
ssh_connection_name=args.ssh_connection_name

configs = {
    'user':args.u,
    'port':args.p,
    'host':args.h
}

if command is None and ssh_connection_name is None:
    out = """
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
            do-droplet-1 : user=ubuntu host=127.0.0.1 port=22
            jolly-haibt : user=root host=137.229.3.12 port=22
            optimistic-wozniak : user=root host=127.0.0.1 port=22
            aws-ec2-3kdf9 : user=ubuntu host=122.2.34.15 port=22

        vssh delete <connection name>
            Deleted elastic-hodgkin

        vssh edit <connection> [-u user -h host -p port]

        vssh <connection>
            Last login: Mon Aug 16 23:56:04 2021 from 174.203.65.152
            root@ubuntu-s-2vcpu-4gb-amd-sfo3-01:~#
    
    """
    print(out)
    exit()


# directories
home_dir = str(Path.home())
app_root_dir = str(Path.cwd())
app_home_dir = os.path.join(home_dir, 'vssh')
system_root_dir = os.path.abspath(os.sep)
ssh_dir = os.path.join(system_root_dir, 'data')
vssh_dir = os.path.join(ssh_dir, 'vssh')
if not os.path.exists(vssh_dir):
    os.makedirs(vssh_dir)



if ssh_connection_name is not None:
    ssh_connection_dir=os.path.join(vssh_dir, ssh_connection_name)


if command == 'list':
    print("\n")
    print("vssh managed ssh connections")
    print("--------------")
    dirs = os.listdir(vssh_dir)
    for dir in dirs:
        new_dir = os.path.join(vssh_dir, dir)
        if os.path.isdir(new_dir):
            with open(f'{new_dir}/vpass-config.yaml', 'r') as yamlfile:
                data = yaml.load(yamlfile, Loader=yaml.SafeLoader)
            print(dir,":", "user=" + data["user"], "host=" + data["host"], "port=" + str(data["port"]))
    print("\n")
    exit()

        
if command == 'create':
    if configs["user"] is None:
        configs["user"] = "root"
    if configs["port"] is None:
        configs["port"] = 22
    if configs["host"] is None:
        configs["host"] = "127.0.0.1"

    if ssh_connection_name is None:
        ssh_connection_name = random_names.run()
        new_ssh_connection_dir = os.path.join(vssh_dir, ssh_connection_name)
    else:
        ssh_connection_name = ssh_connection_name
        new_ssh_connection_dir = os.path.join(vssh_dir, ssh_connection_name)

    new_ssh_connection_dir =  new_ssh_connection_dir

    if not os.path.exists(new_ssh_connection_dir):
        print(f"Creating {ssh_connection_name}")
        os.makedirs(new_ssh_connection_dir)

    # create config file
    with open(f'{new_ssh_connection_dir}/vpass-config.yaml', 'w') as yamlfile:
        data = yaml.dump(configs, yamlfile)

    # create ssh key files
    os.system(f'/bin/bash -c "source ./functions.sh && mutant-ssh-generate-key-static-name {new_ssh_connection_dir}"')
    print("SSH PUBLIC KEY")
    print("--------------------")
    os.system(f'cat {new_ssh_connection_dir}/key.pub')
    print("\n")


    exit()

if command == 'edit':
    # create config file
    with open(f'{ssh_connection_dir}/vpass-config.yaml', 'r') as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.SafeLoader)

        out={}

        # set user
        if configs["user"] is not None:
            out["user"] = configs["user"]
        else:
            out["user"] = data["user"]
        
        # set host
        if configs["host"] is not None:
            out["host"] = configs["host"]
        else:
            out["host"] = data["host"]

        # set port
        if configs["port"] is not None:
            out["port"] = configs["port"]
        elif "port" in data:
            out["port"] = data["port"]
        
    with open(f'{ssh_connection_dir}/vpass-config.yaml', 'w') as yamlfile:
        data = yaml.dump(out, yamlfile)

    exit()

if command == 'delete':
    print(f"Deleted {ssh_connection_name}")
    shutil.rmtree(ssh_connection_dir)
    exit()

if ssh_connection_name is None:
    ssh_connection_name = args.command
    ssh_connection_dir=os.path.join(vssh_dir, ssh_connection_name)
    # create config file
    with open(f'{ssh_connection_dir}/vpass-config.yaml', 'r') as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.SafeLoader)
        print(data)
        
        user = data["user"]
        host = data["host"]
        os.system(f'ssh-keyscan {host} >> /data/known_hosts')
        if "port" in data:
            port = data["port"]
        else:
            port = 22
        
        command = f'ssh -o StrictHostKeyChecking=no -i {ssh_connection_dir}/key {user}@{host}'
        print(command)
        os.system(command)
