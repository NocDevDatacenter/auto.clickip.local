from rich import print
from netmiko import ConnectHandler
"""
Configura uma VLAN no dispositivo Datacom DMOS.
"""


def dot1q_vlan_id(hostname, username, password, vlan, description):
    device = {
        'device_type': 'cisco_ios',
        'host': hostname,
        'username': username,
        'password': password,
        'port': 22,  # Porta SSH padrão
        'timeout': 30,  # Timeout de 30 segundos para a conexão
        'session_timeout': 30,  # Tempo máximo para a sessão SSH
    }

    commands = [
        'config',
        f'dot1q vlan {vlan} name {description} interface ten-gigabit-ethernet-1/1/1 ; top',
        f'commit and-quit label "dot1q" comment "add vlan {vlan} via netmiko"',
        'show dot1q vlan',
    ]

    try:
        ssh = ConnectHandler(**device)
        print(f'[green]Conectado ao Switch {ssh.find_prompt()} - {hostname} ✅[/green]')

        for command in commands:
            output = ssh.send_command(command, expect_string=r'#', read_timeout=15)
            print(output)

    except Exception as e:
        print(f'Error to execute commands:{e}❌')
        output = None

    finally:
        ssh.disconnect()
        print(f'[yellow]Desconectado: {hostname} ⚠️[/yellow]')

    return output
