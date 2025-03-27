from netmiko import ConnectHandler
from app import create_app


def bgp_manager(hostname, username, password, action, group, neighbor):
    app = create_app()

    router = {
        'device_type': 'juniper',
        'host': hostname,
        'username': username,
        'password': password,
        'port': app.config.get('NETMIKO_PORT'),
        'timeout': app.config.get('NETMIKO_TIMEOUT'),
        'session_timeout': app.config.get('NETMIKO_SESSION_TIMEOUT'),
    }

    command_set = f'{action} protocols bgp group {group} neighbor {neighbor}'
    command = f'run show configuration protocols bgp group {group} neighbor {neighbor}'

    try:
        ssh = ConnectHandler(**router)
        ssh.send_config_set(command_set, read_timeout=app.config.get('NETMIKO_TIMEOUT'))
        ssh.commit()
        output = ssh.send_command(command, read_timeout=app.config.get('NETMIKO_TIMEOUT'))

    except Exception as e:
        output = e

    finally:
        ssh.disconnect()

    return output
