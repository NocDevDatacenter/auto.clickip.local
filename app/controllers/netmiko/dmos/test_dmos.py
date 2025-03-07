from netmiko import ConnectHandler
from rich import print


def test_dmos(hostname, username, password):

    device = {
        'device_type': 'cisco_ios',
        'host': hostname,
        'username': username,
        'password': password,
        'port': 22,
        'verbose': True,
        'global_delay_factor': 2,
        'read_timeout_override': 5,
    }

    try:
        ssh = ConnectHandler(**device)
        print(f'[green]Conectado ao {hostname}✅[/green]')

        output = ssh.send_command("show ip interface brief")
        print(output)

    except Exception as e:
        print(f'[red]Error to execute commands: {e}❌[/red]')
        output = None

    finally:
        ssh.disconnect()
        print(f'[yellow]Desconectado do {hostname}⚠️[/yellow]')

    return output
