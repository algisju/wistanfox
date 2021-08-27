#/usr/bin/python3
import requests
from color_t import *
recw=0
with open("tests") as f:
	for line in f:
		line=line.strip()
		try:
			if requests.get("https://"+line,timeout=5):
				print(Color.F_LightGreen,line.ljust(45)+"\t\U0001f44d OK",Color.F_Default)
				recw+=1
				with open("good.txt", 'a') as out:
					out.write(line + '\n')

		except KeyboardInterrupt:
			print(Base.BOLD,Base.FAIL,"\n\U0001F610 You quit by control-c... \n",Base.END)
			break
		except:
			print(Color.F_Cyan,line.ljust(45)+"\t\U0001F628 No access ",Color.F_Default)
	print(f'\nWriting '+str(recw)+'\n')

