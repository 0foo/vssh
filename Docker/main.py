import os, pickle, base64, codecs
from pathlib import Path
import os, shutil, yaml, shutil
from yaml.loader import SafeLoader
import random_names

vssh_data = os.getenv('VSSHDATA')
vssh_data = pickle.loads(codecs.decode(vssh_data.encode(), "base64"))

command = vssh_data["command"]
configs = vssh_data["configs"]

# directories
home_dir = str(Path.home())
app_root_dir = str(Path.cwd())
app_home_dir = os.path.join(home_dir, 'vssh')
system_root_dir = os.path.abspath(os.sep)
ssh_dir = os.path.join(system_root_dir, 'data')
vssh_dir = os.path.join(ssh_dir, 'vssh')
if not os.path.exists(vssh_dir):
    os.makedirs(vssh_dir)

# set default ssh_connetion_dir
ssh_connection_name = None
ssh_connection_dir = None
if vssh_data["ssh_connection_name"] is None:
    if command not in ['list', 'create','edit', 'delete']:
        ssh_connection_name = command
        ssh_connection_dir=os.path.join(vssh_dir, command)
        command = 'run'
    else:
        pass
else:
    ssh_connection_name = vssh_data["ssh_connection_name"]
    ssh_connection_dir=os.path.join(vssh_dir, ssh_connection_name)

if ssh_connection_dir is not None and not os.path.exists(ssh_connection_dir):
    print(f"Please input a valid connection. {ssh_connection_name} does not exist.")
    exit()

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

                req_fields = ['host', 'port', 'note', 'user']

                for item in req_fields:
                    if item not in data:
                        data[item] = "null"

                for key, value in data.items():
                    if value is None:
                        data[key] = "null"

            print(dir,":", "user=" + data["user"], "host=" + data["host"], "port=" + str(data["port"]) ,"note=\"" + data["note"] + "\"")
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
        new_ssh_connection_dir = os.path.join(vssh_dir, ssh_connection_name)

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
    if ssh_connection_dir is None or not os.path.exists(ssh_connection_dir):
        print("Please input a valid connection to edit.")
        exit()
    

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
        
        if configs["note"] is not None:
            out["note"] = configs["note"]
        elif "note" in data:
            out["note"] = data["note"]
        
    with open(f'{ssh_connection_dir}/vpass-config.yaml', 'w') as yamlfile:
        data = yaml.dump(out, yamlfile)

    print(f"Connection {ssh_connection_name} edited successfully.")

    exit()

if command == 'delete':
    if ssh_connection_name is None:
        print("Please input a connection to delete.")
        exit()
    print(f"Deleted {ssh_connection_name}")
    shutil.rmtree(ssh_connection_dir)
    exit()

if command == 'run':
    if ssh_connection_name is None:
            print("Please input a valid connection.")
            exit()
    
    if not os.path.exists(ssh_connection_dir):
        print("Please input a valid connection.")
        exit()

    # load config file
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
        
        command = f'ssh -o StrictHostKeyChecking=no -i {ssh_connection_dir}/key -p {port} {user}@{host}'
        print(command)
        os.system(command)
