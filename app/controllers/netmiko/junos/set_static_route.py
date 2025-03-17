import os
from netmiko import ConnectHandler


# Cria um rota estatica em um dispositivo Juniper
def set_static_route(hostname, username, password, network_dest, next_hop):
    router = {
        'device_type': 'juniper',
        'host': hostname,
        'username': username,
        'password': password,
        'port': os.getenv('NETMIKO_PORT'),
        'timeout': os.getenv('NETMIKO_TIMEOUT'),
        'session_timeout': os.getenv('NETMIKO_SESSION_TIMEOUT'),
    }
    ssh = ConnectHandler(**router)
    ssh.send_config_set(f'set routing-options static route {network_dest} next-hop {next_hop}')
    ssh.commit()
    output = ssh.send_command(f'run show configuration routing-options static route {network_dest} next-hop | display set')
    ssh.disconnect()
    return output
