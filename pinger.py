#!/usr/bin/env python

import subprocess
import sys
import re
import platform
from netaddr import IPNetwork
from concurrent.futures import ThreadPoolExecutor

def ping(ip):
    os_type = platform.system().lower()
    command = ""

    if os_type == "windows":
        command = f"ping -n 1 -w 1000 {ip}"
    else:
        command = f"ping -c 1 -W 1 {ip}"

    result = subprocess.run(command, shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

    if result.returncode == 0:
        print(f"\033[1m\033[92m{ip} responded\033[0m")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '-r':
        print(f"Usage: {sys.argv[0]} -r <Class C network range>")
        sys.exit(1)

    network_range = sys.argv[2]
    if not re.match(r'^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$', network_range):
        print("Invalid network range format. Please use CIDR format (e.g., 192.168.1.0/24).")
        sys.exit(1)

    try:
        network = IPNetwork(network_range)
    except:
        print("Invalid network range. Please check the range.")
        sys.exit(1)

    print(f"[!] Commencing ping sweep against {network_range}...")
    print(f"")

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(ping, network)

if __name__ == "__main__":
    print(f"")
    print(f" ____  _")                       
    print(f"|  _ \(_)_ __   __ _  ___ _ __")
    print(f"| |_) | | '_ \ / _` |/ _ | '__|")
    print(f"|  __/| | | | | (_| |  __| |")   
    print(f"|_|   |_|_| |_|\__, |\___|_|")   
    print(f"               |___/        ")   
    print(f"")
    main()
    print(f"") 
    print(f"[*] ...task completed")
