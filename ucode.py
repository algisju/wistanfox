# !/usr/bin/python3
x=1
print(f'\033[?25l',end=' ')  ## Hide cursor; rstore with print('\033[?25h')
while 1:
	print(f'[\u25e7] EVEN\r',end=' ') if x%2==0 else print(f'[\u25e8] ODD \r',end=' ')
	x=x+1
	if x==10000 :
		x=1
