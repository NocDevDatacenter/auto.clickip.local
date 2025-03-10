import os
from netmiko import ConnectHandler


def get_interface_ae0_config(hostname, username, password, unit):
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
    output = ssh.send_command(f'show configuration interfaces ae0 unit {unit}')
    ssh.disconnect()
    return output
