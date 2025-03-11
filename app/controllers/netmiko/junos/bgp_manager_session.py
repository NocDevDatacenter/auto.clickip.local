import os
from dotenv import load_dotenv
from netmiko import ConnectHandler

load_dotenv()


def bgp_manager_session(hostname, username, password, action, group, neighbor):

    router = {
        'device_type': 'juniper',
        'host': hostname,
        'username': username,
        'password': password,
        'port': os.getenv('NETMIKO_PORT'),
        'timeout': os.getenv('NETMIKO_TIMEOUT'),
        'session_timeout': os.getenv('NETMIKO_SESSION_TIMEOUT'),
    }

    command_set = f'{action} protocols bgp group {group} neighbor {neighbor}'
    command = f'show configuration protocols bgp group {group} neighbor {neighbor}'

    try:
        ssh = ConnectHandler(**router)
        ssh.send_config_set(command_set, read_timeout=15)
        # ssh.commit() not yet implemented
        output = ssh.send_command(command, read_timeout=15),

    except Exception as e:
        output = e

    finally:
        ssh.disconnect()

    return output
