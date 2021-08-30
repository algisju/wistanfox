#/usr/bin/python3
from paramiko import *

client = SSHClient()
client.load_system_host_keys()
try:
	client.connect('192.168.0.125',port=22, username="pi", password="4313")
	print("It Connected")
	print(client.exec_command('ls -l'))
except:
	print("Can\'t Connect")
