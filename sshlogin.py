import pexpect


PROMPT = ['# ','>>> ', ' $', '\$ ', '~ $ ', 'PIBOX:~ $ ','$']

def send_command(child,command):
	child.sendline(command)
	print child
	child.expect(PROMPT)

def connect(user,host,password):
	ssh_newkey='Are you sure you want to continue connecting'
	connStr='ssh '+user+'@'+host
	child=pexpect.spawn(connStr)
	ret=child.expect([pexpect.TIMEOUT, ssh_newkey, '[Pp]assword: '],timeout=3)
	if ret==0:
		print '[-] Error Connecting'
		return
	if ret==1:
		child.sendline('yes')
		ret=child.expect([pexpect.TIMEOUT,'[Pp]assword: '])
		if ret==0:
			print '[-] Error pass'
			return

	child.sendline(password)
	child.expect(PROMPT,timeout=0.5)
	return child


def main():
	host='192.168.0.125'
	user='pi'
	password='4313'
	child=connect(user,host,password)
	send_command(child,'whoami')
	print 'after func, no err'

main() 

