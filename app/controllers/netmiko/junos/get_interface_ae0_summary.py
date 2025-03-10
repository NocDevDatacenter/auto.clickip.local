import os
from netmiko import ConnectHandler


# Retrieves the interface summary from a Juniper device
def get_interface_ae0_summary(hostname, username, password):
    router = {
        'device_type': 'juniper',  # Specifies the device type as Juniper
        'host': hostname,  # Hostname or IP address of the target device
        'username': username,  # Login username
        'password': password,  # Login password
        'port': os.getenv('NETMIKO_PORT'),  # Retrieves SSH port from environment variables
        'timeout': os.getenv('NETMIKO_TIMEOUT'),  # Sets connection timeout from environment variables
        'session_timeout': os.getenv('NETMIKO_SESSION_TIMEOUT'),  # Sets session timeout from environment variables
    }

    # Establish an SSH connection to the device
    ssh = ConnectHandler(**router)

    # Execute the command to display a summary of the loopback interface (lo0)
    output = ssh.send_command('show interfaces terse lo0 | match lo')

    # Close the SSH connection
    ssh.disconnect()

    return output  # Returns the command output
