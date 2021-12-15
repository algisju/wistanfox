import socket
import ssl

hostname = '192.168.0.124'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

def unit1():
    pass

def unit2():
    pass

print("😂")
