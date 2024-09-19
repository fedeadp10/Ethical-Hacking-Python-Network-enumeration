THIS IS A DRAFT ! ! ! 

# Ethical-Hacking-Python-Network-enumeration
Simple Python script designed for basic network enumeration and port scanning, often used in penetration testing.
# Network Enumeration & Pentesting Script

This project provides a simple Python script for network enumeration and port scanning. It can identify live hosts on a network and check for open ports, which is often a key part of penetration testing.

## Features
- **Ping Sweep**: Identifies live hosts on a `/24` network using the `ping` command.
- **Port Scanning**: Scans live hosts for open ports (defaults to common service ports like HTTP, SSH, etc.).
- **Cross-Platform**: Works on both Windows and Linux/Mac by adjusting the `ping` command automatically.

## Usage
1. Run the script:
   When prompted, enter the base network to scan (e.g., 192.168.1 for 192.168.1.0/24).
2. Example Input:
   Enter the network to scan (e.g., 192.168.1): 192.168.1
3. The script will perform a ping sweep to find live hosts and then port scan each live host for open ports. Results will be displayed in the terminal.

## Requirements
Python 3.x
Standard libraries: socket, subprocess, os, platform, concurrent.futures
This script is a basic implementation for network enumeration and port scanning and can be expanded further depending on your needs.

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
