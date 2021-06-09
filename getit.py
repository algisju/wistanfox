#!/usr/bin/env python 3+
# -*- coding: utf-8 -*-
#
#  getit.py
#  multi-threading email check format validation and online existence
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
# ******** TO DO COMMENT LINE args ******************

import sys, getopt, requests, time
import concurrent.futures
from validate_email import validate_email

count=0
okcount=0

def check_key(thekey):


	if validate_email(client_email[0:client_email.index(':')],verify=True) :
		print(f'\033[92m{client_email[0:client_email.index(":")]:35} => OK')
#				color	{	variable extract					:35} is TABULATION		
		b_file = open('clean_combos.6.btc','a') 
		b_file.write(client_email+'\n')
		c_file = open('clean_mails.6.btc','a') 
		c_file.write(client_email[0:client_email.index(":")]+'\n')
		okcount+=1
		return True
	else:
		print(f'\033[91m{client_email[0:client_email.index(":")]:35} * NOT OK *')
		d_file = open('unverified.6.btc','a') 
		d_file.write(client_email+'\n')
		return False  
	
with open('BTC_in.txt','r') as a_file:
	for line in a_file:
		client_email=a_file.read().splitlines()
		count+=1
		with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
			if executor.map(check_key, thekey):
				okcount+=1
	print(f'\033[0mFinished: Total: {count} Existing: {okcount}')
