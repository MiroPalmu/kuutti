import chi
import chi.lease
import chi.server
from chi.ssh import Remote
import sys

chi.set('project_id', '9a85895b81ee42b09a13d980690f2390')
chi.use_site('CHI@UC')    #Set which site to use

login_server_ip = "10.140.83.107"
common_server_prefix = "kuutti"

# Check for ports open
all_ports = chi.network.list_ports()

login_hostname = None
compute_static_ips_with_names = []

def clean_server_name(server: str):
    '''
    str(chi.server.get_server(x['device_id'])) return the name in form:
    <Server: hostname>

    so this function strips <Server: and > away so we just get the hostnmae
    '''
    return server[9:-1]

for x in all_ports:
    try:
        instance_name = clean_server_name(str(chi.server.get_server(x['device_id'])))
        if common_server_prefix not in instance_name:
            continue
        ip_settings = x['fixed_ips']
        static_ip = ip_settings[0]['ip_address']
        print(static_ip)
        if static_ip in login_server_ip:
            login_hostname = instance_name
        else:
            compute_static_ips_with_names.append((static_ip, instance_name))
    except Exception as e:
        continue

with open("inventory.yml", "w") as inv:
    if login_hostname == None:
        raise Exception(f"Did not find login host based on login_server_ip: {login_server_ip}")
    inv.write("[login_server]\n")
    inv.write(f"{login_hostname} ansible_host={login_server_ip} ansible_user=cc\n\n")
    inv.write("[compute_servers]\n")

    for ip, hostname in compute_static_ips_with_names:
        print(f"Added {ip} to compute_servers")
        inv.write(f"{hostname} ansible_host={ip} ansible_user=cc\n")
