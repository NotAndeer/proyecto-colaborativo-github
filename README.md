# NetScan Web

Aplicación web para verificar qué dispositivos están activos en una red local.

## Tecnologías

- Backend: Python + Flask
- Frontend: HTML, CSS, JavaScript

## Requisitos

- Python 3.6 o superior
- Flask

## Instalación y ejecución

1. Clona el repositorio:
   ```bash
   git clone https://github.com/NotAndeer/proyecto-colaborativo-github.git
   cd proyecto-colaborativo-github

Instala las dependencias:

pip install -r requirements.txt
Ejecuta el servidor:

python app.py
Abre tu navegador y visita:

http://localhost:5000
Funcionalidad principal
Escanea dispositivos activos en una red local dentro de un rango IP definido.

Ejemplo de función principal en scanner.py
python
Copiar
Editar
import os

def scan_network(ip_base, start, end):
    """
    Escanea una red local en busca de dispositivos activos.

    Parámetros:
    - ip_base: parte fija de la IP, ej. "192.168.1"
    - start: inicio del rango
    - end: fin del rango

    Retorna:
    - lista de IPs activas
    """
    active_ips = []
    for i in range(start, end + 1):
        ip = f"{ip_base}.{i}"
        response = os.system(f"ping -c 1 {ip}")
        if response == 0:
            print(f"{ip} está activo")
            active_ips.append(ip)
        else:
            print(f"{ip} no responde")
    return active_ips
Ejemplo de salida
Al escanear la red 192.168.1.0 para hosts del 1 al 10:

python-repl
Copiar
Editar
192.168.1.1 está activo
192.168.1.2 no responde
192.168.1.3 está activo
...
192.168.1.10 está activo

