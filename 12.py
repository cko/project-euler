import math

divcount=0
sumnatural=0
natural=1
maxdivcount=0
while divcount < 500:
	sumnatural = sumnatural + natural
	#print "sumnatural" + str(sumnatural) 
	divcount=2
	rangestart= int(math.ceil(math.sqrt(sumnatural)))

	for i in range(2,rangestart):
		if sumnatural%i == 0:
			divcount = divcount+1
			if sumnatural/i > rangestart:
				divcount = divcount +1		

	natural=natural+1
	if divcount>maxdivcount:	
		print str(divcount) + "  " + str(sumnatural)
		maxdivcount=divcount
print sumnatural
	
