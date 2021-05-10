#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sortcsv.py
#  sorting csv airodump-ng to parse with other hacking shit
#  geek <geek@KALIBOX>
#  
#  
def checkcsv():
	import csv,json
	print("Declotting step 1...\n\n")
	with open('step1-01.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			print(json.dumps(row,indent=4))

def main(args):
	return 0

if __name__ == '__main__':
	import sys
	checkcsv()
	sys.exit(main(sys.argv))
	
