# !/usr/bin/python
import socket


def grab_banner(ip_address, port):
    try:
        s = socket.socket()
        s.settimeout(2.0)
        s.connect((ip_address, port))
        banner = s.recv(1024)
        s.close()
        return banner if (type(banner)=='str') else str(banner,'utf-8')
    except:
        return 'Screw it...\n'


def main():
    ports = [22,80,443,3389]
    for port in ports:
        ip_address = '192.168.0.124'
        print((ip_address+":"+str(port))+(" : "+grab_banner(ip_address, port)),end='')
if __name__ == '__main__':
    main()
