import time
import math

bigprim=3
newvalue=3
oldtime=0;
summe=5;
while True:
#while bigprim<2000000L:
	newvalue = newvalue + 2;
	isPrime=True;
	rangestart= math.ceil(math.sqrt(newvalue))+1;
	if rangestart%2 == 0:
		rangestart=rangestart-1;
	for i in range(rangestart,2,-2):
		rest = newvalue % i;
		if (rest == 0):		
			isPrime=False;
	if isPrime:
		bigprim=newvalue;	
		if bigprim > 2000000L:
			break;
		newtime=time.clock();
		diff=newtime-oldtime;
		#print str(bigprim) #+ "\t" + str(time.clock()) + "\t" + str(diff);
		oldtime=newtime;
		summe=summe+bigprim;
		print summe;
