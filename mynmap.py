#!/usr/bin/env python 3.8+
# -*- coding: utf-8 -*-
#
#  mynmap.py
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
import optparse
import socket
from socket import *

def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect(tgtHost, tgtPort)
		connSkt.send('ViolentPython\r\n')
		results = connSkt.recv(100)
		print('[+]%d/tcp open'%tgtPort)
		print('[+] ' + str(results))
		connSkt.close()
	except:
		print('[-]%d/tcp close'%tgtPort)
		
def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print("[-] Cannot Resolve'%s': Unknown Host "%tgtHost)
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print('\n[+] Scan Results for: ' + tgtName[0])
	except:
		print('\n[+] Scan Results for: ' + tgtIP)
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print('Scanning Port ' + str(tgtPort)+'...')
		connScan(tgtHost, int(tgtPort))




def main(args):
	parser = optparse.OptionParser('usage %prog –H '+\
		'<target host> -p <target port>')
	parser.description='Very bad copy of nmap: mainly a test for argument passing parsing text epilogue etc...'
	parser.epilog='Be yourself; everyone else is already taken.  --Oscar Wilde'
	parser.add_option('-H', dest='tgtHost', type='string', \
		help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', \
		help='specify target port')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPorts == None):
		print(parser.usage)
		exit(0) 
	portScan(tgtHost, tgtPorts)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
