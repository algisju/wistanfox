#!/usr/bin/env python3  
import sys,argparse
from socket import socket, AF_INET, SOCK_STREAM
# For debug
#import pdb; pdb.set_trace()
VERSION = '0.0'
welcome = b"Debian X64\nVersion 11.2/LTS\n login: "

def send_email(src_address):
    """ Todo: send an email / alarm """
    pass

def honeypot(address,port=23):
    """ create a single Threaded telnet listen port """
    try:
        ski=socket(AF_INET,SOCK_STREAM)
        ski.bind((address, port))
        ski.listen()
        conn,addr = ski.accept()
        print('honeypot has been visited by ' + addr[0])
        send_email(addr[0])
        conn.sendall(welcome)
        while True:
            data=conn.recv(1024)
            if data == b'\r\n':
                ski.close()
                sys.exit()
    except: 
        ski.close()
        sys.exit()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Honeypot test',
                                 epilog='Version: ' + str(VERSION))
    parser.add_argument('-a','--address',help='server ip address to use',action='store', required=True)   
    args = parser.parse_args()
    
    honeypot(args.address)
