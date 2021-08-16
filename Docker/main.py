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


# directories
home_dir = str(Path.home())
app_root_dir = str(Path.cwd())
app_home_dir = os.path.join(home_dir, 'vssh')
system_root_dir = os.path.abspath(os.sep)
ssh_dir = os.path.join(system_root_dir, 'data')
if ssh_connection_name is not None:
    ssh_connection_dir=os.path.join(ssh_dir, ssh_connection_name)





if command == 'create':
    if configs["user"] is None:
        configs["user"] = "root"
    if configs["port"] is None:
        configs["port"] = 22
    if configs["host"] is None:
        configs["host"] = "127.0.0.1"

    if ssh_connection_name is None:
        dir_name = random_names.run()
        new_ssh_connection_dir = os.path.join(ssh_dir, dir_name)
    else:
        ssh_connection_name = ssh_connection_name
        new_ssh_connection_dir = os.path.join(ssh_dir, ssh_connection_name)

    new_ssh_connection_dir =  new_ssh_connection_dir

    if not os.path.exists(new_ssh_connection_dir):
        print(f"Creating {new_ssh_connection_dir}")
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
    print(f"Deleting {ssh_connection}")
    shutil.rmtree(ssh_connection_name)
    exit()

if ssh_connection_name is None:
    ssh_connection_name = args.command
    ssh_connection_dir=os.path.join(ssh_dir, ssh_connection_name)
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


# def list():
#     dirs = os.listdir(ssh_dir)
#
#     print("")
#     print("All vssh managed SSH options")
#     print("------")
#     for dir in dirs:
#         if os.path.isdir(os.path.join(ssh_dir, dir)) and 'vssh' in dir:
#             print(dir)
#     print("\n")
#     exit()
#
# if command == 'delete':
#     pass
#
# if command == 'go':
#     pass