# Ethical-Hacking-Python-Network-enumeration
Simple Python script designed for basic network enumeration and port scanning, often used in penetration testing.
# Network Enumeration & Pentesting Script

This project provides a simple Python script for network enumeration and port scanning. It can identify live hosts on a network and check for open ports, which is often a key part of penetration testing.

## Features
- **Ping Sweep**: Identifies live hosts on a `/24` network using the `ping` command.
- **Port Scanning**: Scans live hosts for open ports (defaults to common service ports like HTTP, SSH, etc.).
- **Cross-Platform**: Works on both Windows and Linux/Mac by adjusting the `ping` command automatically.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/network-enum-pentest.git
   cd network-enum-pentest
2. Run the script
  python scan_network.py
3. Enter the base IP (eg. 192.168.0.1)
   Enter the base IP (e.g., 192.168.1): 192.168.1
4. The script will identify live hosts and scan the common ports:
  Ports: 22 (SSH), 80 (HTTP), 443 (HTTPS), 445 (SMB), 3389 (RDP).
# Example output
Scanning network: 192.168.1.0/24
192.168.1.5 is live!
Open ports on 192.168.1.5: [22, 80]
192.168.1.10 is live!
Open ports on 192.168.1.10: []
