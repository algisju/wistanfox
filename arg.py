#/usr/bin/python3
"""
	Check Network  Access from file list - by Geek\'s Gang
			Version 0.0
			
Usage:
  arg.py -i FILE [-o FILE] [-t THREADS]
  arg.py (-h | --help)
  arg.py --version

Options:
  -i		Input file name 
  -o		Output results filename [default: output.txt]
  -t		Number of threads [default: 10]
  -h --help     Show this screen.
  --version     Show version.
  
"""
import requests
from docopt import docopt
from color_t import *
from concurrent.futures import ThreadPoolExecutor, as_completed

def checkit(line):
	global recw
	try:
		if requests.get("https://"+line,timeout=5):
			print(Color.F_LightGreen,line.ljust(45)+"\t\U0001f44d OK",Color.F_Default)
			recw+=1
			with open(outfile, 'a') as out:
				out.write(line + '\n')
	except:
		print(Color.F_Cyan,line.ljust(45)+"\t\U0001F628 No access ",Color.F_Default)
	return 0
	
if __name__ == '__main__':
    print("\033c")
    recw=0
    arguments = docopt(__doc__, version='ARG 0.0')
    infile=arguments['-i']; outfile=arguments['-o']; nthreads=arguments['-t']
    outfile = arguments['-o'] if outfile  else "output.txt"
    nthreads = int(arguments['-t']) if nthreads else 10
    print("\033c"+Base.BOLD,"\n\tInput: "+infile+" Output: "+outfile+" Threads: "+str(nthreads)+"\n",Base.END)
    f=open("tests",'r')
    processes = []
    with ThreadPoolExecutor(max_workers=nthreads) as executor:
        for line in f:
            line=line.strip()
            try:
                processes.append(executor.submit(checkit,line))
            except KeyboardInterrupt:
                executor.shutdown(wait = True, cancel_futures = True)
                print(Base.BOLD,Base.FAIL,"\n\U0001F610 You quit by control-c... \n",Base.END)
    print(Base.BOLD,"\n\tAccessible: "+str(recw)+" entries, results in "+outfile+"\n", Base.END)
