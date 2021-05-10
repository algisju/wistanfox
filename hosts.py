import nmap
from elevate import elevate
nm = nmap.PortScanner()
elevate(graphical=False)
print("Scanning Net...")
nm.scan(hosts='192.168.0.1/24', arguments='-sS -O')
for host in nm.all_hosts():
	print(host)
	print(nm[host].get('osclass', 'unknown'))
	# {'vendor': 'Linux', 'accuracy': '100', 'type': 'general purpose',
	#  'osfamily': 'Linux', 'osgen': '3.X'}
	#print the host and the Operating system
	
import subprocess
subprocess.run(["besside-ng", "-h"])

