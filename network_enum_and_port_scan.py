import os
import platform
import subprocess
import socket
from concurrent.futures import ThreadPoolExecutor

# Ping a host to see if it is up
def ping_sweep(ip):
    # Determine the system platform to use the correct ping command
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]

    try:
        # Run the ping command
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return True  # If ping was successful
    except subprocess.CalledProcessError:
        return False  # If ping failed

# Scan for open ports on a host
def port_scan(ip, ports=[22, 80, 443]):  # Default common ports: SSH, HTTP, HTTPS
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Main function for network scanning
def network_enumeration(network):
    print(f"Scanning network {network}.0/24...")
    
    live_hosts = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Create a list of IP addresses in the /24 network range
        ip_addresses = [f"{network}.{i}" for i in range(1, 255)]
        results = list(executor.map(ping_sweep, ip_addresses))
        
        # Collect the live hosts
        for i, is_alive in enumerate(results):
            if is_alive:
                live_hosts.append(ip_addresses[i])
    
    print(f"Live hosts found: {live_hosts}")
    print("Scanning ports on live hosts...")

    # Scan ports on the live hosts
    for host in live_hosts:
        open_ports = port_scan(host)
        if open_ports:
            print(f"Host {host} has open ports: {open_ports}")
        else:
            print(f"Host {host} has no open ports.")

if __name__ == "__main__":
    # Specify the base network (e.g., "192.168.1" for a 192.168.1.0/24 network)
    network = input("Enter the network to scan (e.g., 192.168.1): ")
    network_enumeration(network)
