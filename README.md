# Provision instructions

Assume that headnode and compute nodes are created, st. compute nodes are accessible from headnode. See step 5) for naming.

Sometimes during first run of playbook there is problems with `/bin/python` no being found. Just run the playbook again and it shloud fix itself.

1) ssh to headnode
2) create a ssh key of type rsa
3) add wanted keys to authorize keys (including headnode´s own ssh key!)
4) close ssh connection
5) Crete inventory.yml
    - It has to contain groups:
        - `login_server`
            - With only one entry
        - `compute_servers`
            - Hostnames of compute_servers must be in form `<kuutti_computenode_common_hostname_prefix>-<ordinal_number>`
    - Hosts are given in form `<hostname> ansible_host=<local_ip> ansible_user=<user_that_ansible_ssh_into>`
        - kuutti role assumes at some point that dir `/home/<user_that_ansible_ssh_into>/` exists

If using openstack `create_inventory.py` script can help (remember to modify variables inside).

6) Copy kuutti to floating ip with:

```scp -r -O <path_to_kuutti> cc@$FLOATING_IP:/home/cc```

7) ssh to loginnode
8) install required ansible stuff with:

```
ansible-galaxy install -r requirements.yml
ansible-galaxy collection install -r requirements.yml
```

9) Set variables in `vars/main.yml`

    - Set user names in `vars/main.yml` users variable as list of the user names
    - Also set kuutti_path_to_user_public_keys to full path of directory containg pulic keys of users in format `<user_name>.pub`

)

```
ANSIBLE_REMOTE_TMP=/tmp ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory.yml provision_computenodes.yml
```

# Removed steps (only for historic purposes)

- save floating ip of loging node as FLOATING_IP
- save the public key of loging node as LOGIN_PUB

```
LOGIN_PUB='<public_key>'
```

- Append login node public key to all servers authorized keys: (ssh command will also be run for all ips (static and floating) in the project. It will fail for the oneas that do not have right keys setup and id does not matter if it succeess for floating)

```
openstack server list | grep -oE '([[:digit:]]{1,3}\.){3}[[:digit:]]{1,3}' | while read ln; do ssh -o StrictHostKeyChecking=no -J cc@$FLOATING_IP cc@$ln "echo '$LOGIN_PUB' >> .ssh/authorized_keys" < /dev/null; done
```
