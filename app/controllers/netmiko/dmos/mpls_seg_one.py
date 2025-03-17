from rich import print
from netmiko import ConnectHandler
"""
Configura uma VLAN no dispositivo Datacom DMOS.
"""

def mpls_seg_one(hostname, username, password, vlan, description, ipv4_neighbor):
    switch = {
        'device_type': 'cisco_ios',
        'host': hostname,
        'username': username,
        'password': password,
        'port': 22,  # Porta SSH padrão
        'timeout': 30,  # Timeout de 30 segundos para a conexão
        'session_timeout': 30,  # Tempo máximo para a sessão SSH
    }

    try:
        ssh = ConnectHandler(**switch)
        print(f'[green]Conectado ao {hostname}✅[/green]')

        commands = [
            'config exclusive',
            f'mpls l2vpn vpls-group tunnel-{vlan} vpn {description} description "{description}" administrative-status up',
            f'mpls l2vpn vpls-group tunnel-{vlan} vpn {description} vfi pw-type vlan {vlan} neighbor {ipv4_neighbor} pw-id {vlan} pw-mtu 1600 pw-load-balance flow-label both',
        ]

        for command in commands:
            output = ssh.send_command(command, expect_string=r'#', read_timeout=15)

            # 'config exclusive',
            # f'mpls l2vpn vpls-group tunnel-{vlan}'           \
            #     'vpn {description}'                           \
            #         'description "{description}"' ;           \
            #     administrative-status up',
            # f'mpls l2vpn vpls-group tunnel-{vlan}           \
            #     vpn {description} ;                         \
            #         vfi                                     \
            #             pw-type vlan {vlan} ;               \
            #             neighbor {ipv4_neighbor} pw-id {vlan} ; \
            #             pw-mtu 1600 ;                       \
            #             pw-load-balance                     \
            #                 flow-label both',
            # f'mpls l2vpn vpls-group tunnel-{vlan}           \
            #     vpn {description} ;                         \
            #         bridge-domain                           \
            #             dot1q {vlan} ;                      \
            #             access-interface ten-gigabit-ethernet-1/1/1',
            # 'commit confirmed 3; top',
        # ]

        # output = ssh.send_command('show mpls l2vpn vpls brief', expect_string=r'#')

        # ssh.send_command('config exclusive', expect_string=r'#')

        # ssh.send_command(  # descricao do VPLS
        #     f'mpls l2vpn vpls-group tunnel-{vlan}           \
        #         vpn {description}                           \
        #             description "{description}" ;           \
        #         administrative-status up', expect_string=r'#'d
        #     )

        # ssh.send_command(
        #     f'mpls l2vpn vpls-group tunnel-{vlan}           \
        #     vpn {description} ;                             \
        #         vfi                                         \
        #             pw-type vlan {vlan} ;                   \
        #             neighbor {ipv4_neighbor} pw-id {vlan} ; \
        #             pw-mtu 1600 ;                           \
        #             pw-load-balance                         \
        #                 flow-label both', expect_string=r'#'
        #     )

        # ssh.send_command(
        #     f'mpls l2vpn vpls-group tunnel-{vlan}           \
        #     vpn {description} ;                             \
        #         bridge-domain                               \
        #             dot1q {vlan} ;                          \
        #             access-interface ten-gigabit-ethernet-1/1/1', expect_string=r'#'
        #     )

        # ssh.send_command('commit confirmed 3; top', expect_string=r'#')

        # output = ssh.send_command(f'show mpls l2vpn vpls-group brief | include {vlan}', expect_string=r'#')

        # print(output)

    except Exception as e:
        print(f'Error to execute commands:{e}❌')
        # output = None

    finally:
        ssh.disconnect()
        print(f'[yellow]Desconectado do {hostname}⚠️[/yellow]')

    # return output
