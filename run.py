import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

print("Simple Python Scanner by Eff3ct")

host = input("[*] Please enter the IP you want to scan [*]: ")
port = int(input("[*] Please enter the port you want to scan [*]:"))

print("[*] Scanning Target... [*]")


def portScanner(port):
    if s.connect_ex((host, port)):
        print("Ops The port is closed")
    else:
        print("Ops! The port is open")


portScanner(port)
