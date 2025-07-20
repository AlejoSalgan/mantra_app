import os

def escanear_ip(ip):
    respuesta = os.system(f"ping -n 1 {ip}")

    if respuesta == 0:
        print(f"[+] IP Activa: {ip}")
    else:
        print(f"[+] IP Inactiva: {ip}")
escanear_ip("192.168.0.15")