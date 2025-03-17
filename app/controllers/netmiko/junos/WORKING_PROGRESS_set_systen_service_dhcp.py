import os
import sys
from netmiko import ConnectHandler

# Corrige o caminho para encontrar config.py
config_path = os.path.abspath("app/controllers/netmiko/junos")
sys.path.append(config_path)


def set_access_address_assignment(
    hostname, username, password,
    vlan_id, ipv4_gateway, pool_name,
    network, address_low, address_high
):
    """Configura o serviço DHCP no roteador Junos via Netmiko."""

    router = {
        'device_type': 'juniper',
        'host': hostname,
        'username': username,
        'password': password,
        'port': os.getenv('NETMIKO_PORT'),
        'timeout': os.getenv('NETMIKO_TIMEOUT'),
        'session_timeout': os.getenv('NETMIKO_SESSION_TIMEOUT'),
    }

    try:
        ssh = ConnectHandler(**router)

        commands = [
            f'set interfaces ae0 unit {vlan_id} vlan-id {vlan_id} description "{pool_name}" family inet address {ipv4_gateway}/21',
            f'set system services dhcp-local-server group DHCP-IPHOST-WIRE interface ae0.{vlan_id}',
            f'set access address-assignment pool {pool_name} family inet network {network}/21',
            f'set access address-assignment pool {pool_name} family inet range address low {address_low}',
            f'set access address-assignment pool {pool_name} family inet range address high {address_high}',
            f'set access address-assignment pool {pool_name} family inet dhcp-attributes maximum-lease-time 604800',
            f'set access address-assignment pool {pool_name} family inet dhcp-attributes server-identifier {ipv4_gateway}',
            f'set access address-assignment pool {pool_name} family inet dhcp-attributes router {ipv4_gateway}',
            f'set access address-assignment pool {pool_name} family inet dhcp-attributes option 43 string "http://172.25.200.38:7547 dmview dmview datacom datacom"',
        ]

        ssh.send_config_set(commands, read_timeout=15)
        ssh.commit()

        # Executa os comandos de verificação corretamente
        output = [
            ssh.send_command(f'run show configuration interfaces ae0 unit {vlan_id}\n'),
            ssh.send_command(f'run show configuration access address-assignment pool {pool_name}'),
        ]

        # Exibe a saída formatada corretamente
        for line in output:
            print(line)

    except Exception as e:
        output = e

    finally:
        ssh.disconnect()

    return output
