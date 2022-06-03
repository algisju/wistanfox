import arpreq

# construct ip subnet

sub1='192.168.0.'

for x in range(255):
	sub2=sub1+str(x)
	if arpreq.arpreq(sub2) != None:
		print(sub2+'  '+arpreq.arpreq(sub2)) 
