# need pip install netifaces and interfaces on windows systems
### List network Interfaces and the associated IP ##
#!/usr/bin/env python
from netifaces import interfaces, ifaddresses, AF_INET
from requests import get
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    print('%s: %s' % (ifaceName.ljust(18), ', '.join(addresses)))
extip=get('https://api.ipify.org').text
print("wanip".ljust(18)+": "+extip)
