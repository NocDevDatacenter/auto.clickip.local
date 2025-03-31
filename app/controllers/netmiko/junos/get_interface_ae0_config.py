from app import create_app
from netmiko import ConnectHandler


def get_interface_ae0_config(hostname, username, password, unit):
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
    ssh = ConnectHandler(**router)
    output = ssh.send_command(f'show configuration interfaces ae0 unit {unit}')
    ssh.disconnect()
    return output
