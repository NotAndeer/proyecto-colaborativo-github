import os
import platform
import subprocess

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    try:
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_network(base_ip):
    hosts = []
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            hosts.append({'ip': ip, 'status': 'Activo'})
    return hosts
