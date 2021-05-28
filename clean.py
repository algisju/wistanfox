#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clean.py
#  Take any text file input treat it
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
#  
import argparse

#IF LI LING IS WATCHING THEN:
#	CLOSE WINDOW

def main():
	if sys.version_info < (3,0):
		print("ERROR: CredNinja runs on Python 3.  Run as \"./CredNinja.py\" or \"python3 CredNinja.py\"!")
		sys.exit(1)
	args = parse_cli_args()
	hosts = []
	creds = []
	print('Ha!')
	return 0


def parse_cli_args():
    parser = argparse.ArgumentParser(add_help=False, description='Quickly check the validity of multiple user credentials across multiple servers and be notified if that user has local administrator rights on each server.')

    mandatory_args = parser.add_argument_group('Required Arguments')
    mandatory_args.add_argument('-a','--accounts', default=None, required=True, metavar='accounts_to_test.txt', help='A word or file of user credentials to test. Usernames are accepted in the form of "DOMAIN\\USERNAME:PASSWORD"')
    mandatory_args.add_argument('-s', '--servers', default=None, required=True, metavar='systems_to_test.txt', help='A word or file of servers to test against. This can be a gnmap file or contain cidr ip addresses. Each credential will be tested against each of these servers by attempting to browse C$ via SMB')
 
    optional_args = parser.add_argument_group('Optional Arguments')
    optional_args.add_argument('-t', '--threads', default=10, type=int, help='Number of threads to use. Defaults to 10')

    optional_args.add_argument('-p', '--passdelimiter', default=':', help='Change the delimiter between the account username and password. Defaults to ":"')

    additional_args = parser.add_argument_group('Additional Information Retrieval')
    additional_args.add_argument('--os', default=False, action='store_true', help='Display the OS of the system if available (no extra request is being sent)')
    args = parser.parse_args()
    if args.accounts is None or args.servers is None:
        parser.print_help()
        sys.exit()
    return args
    print(args)







if __name__ == '__main__':
    import sys
    sys.exit(main())
