#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Generate datebirth password lists
# yyyymmdd ddmmyyyy mmddyyyy
# 365 days/year= 1,095 try/year 40 years=43,800 pwd generated
# Generate Taiwan mobile phone numbers password lists
# Prefixe xxx-xxx
# 1M numbers/43 prefixes= 43M numbers
#
#  genpass.py
#  
#  Copyright 2021 geek <geek@KALIBOX>
#  
from color_t import *
from numba import jit

#@jit(nopython=True)
def phonepass():
	phone_prefix=["905","912","932","962","965","967","968","969","910","911","919","921","928","933","937",
	"913","915","916","917","925","926","927","930","931","936","938","955","939","968","966","918","920","922",
	"923","929","935","939","952","953","956","958","970","986","978","973"]	# MOBILE PHONES PREFIXES TAIWAN
	xcount=0
	for i in phone_prefix:
		for j in range(0,1000):
			for k in range(0,1000):
				print(f"{Color.F_LightGreen}Current Number: {Color.F_LightRed}0{i}{j:03}{k:03}{Color.F_LightGreen} - Current Prefix: {Color.F_LightRed}0{i}{Color.F_LightGreen} - Total: {Color.F_LightRed}{xcount:,}",end="\r")
				#afile=open('mobiles-twn.pwd','a')
				#afile.write(f"0{i}{j:03}{k:03}\n")
				
	# for i in range(1975,2011):		# YEARS
		# for j in range(1,13):		# MONTHS
			# for k in range(1,32):	# DAYS
				# print(f"{i}{j:02}{k:02} yyyymmdd")
				# print(f"{k:02}{j:02}{i} ddmmyyyy")
				# print(f"{j:02}{k:02}{i} mmddyyyy")
				# afile = open('birthdates.pwd','a') 
				# afile.write(f"{i}{j:02}{k:02}\n")
				# afile.write(f"{k:02}{j:02}{i}\n")
				# afile.write(f"{j:02}{k:02}{i}\n")
				xcount +=1				
	print(f"{Color.F_LightRed}\n\n{xcount:,}{Color.F_LightGreen} Written")
	
	
def main(args):
	phonepass()
	#writepass()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
