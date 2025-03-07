import ipaddress


def ipcalc(network):
    hosts = ipaddress.ip_network(network, strict=False)

    first_host = hosts.network_address + 1
    second_host = hosts.network_address + 2
    last_host = hosts.broadcast_address - 1

    return [
        first_host,
        second_host,
        last_host,
    ]
