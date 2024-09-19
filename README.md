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
