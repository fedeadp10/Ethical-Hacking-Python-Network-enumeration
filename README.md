# Ethical-Hacking-Python-Network-enumeration
Simple Python script designed for basic network enumeration and port scanning, often used in penetration testing.
# Network Enumeration & Pentesting Script

This project provides a simple Python script for network enumeration and port scanning. It can identify live hosts on a network and check for open ports, which is often a key part of penetration testing.

## Features
- **Ping Sweep**: Identifies live hosts on a `/24` network using the `ping` command.
- **Port Scanning**: Scans live hosts for open ports (defaults to common service ports like HTTP, SSH, etc.).
- **Cross-Platform**: Works on both Windows and Linux/Mac by adjusting the `ping` command automatically.

## Usage
