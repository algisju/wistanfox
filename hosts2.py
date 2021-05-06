#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hosts2.py  
#  
import json
import nmap3


def discoverhosts():
    print("Discovering Hosts...")
    network = nmap3.Nmap()
    results = network.scan_top_ports("192.168.0.1/24", args="-sn")

    with open("Network_discover", 'w') as json_file:
        json.dump(results, json_file, indent=4)

    return 0


def main(args):
    discoverhosts()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
