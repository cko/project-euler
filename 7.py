import time
import math

primcount=2
bigprim=3
newvalue=3
oldtime=0;
#while primcount<10001:
while primcount<6:
	newvalue = newvalue + 2;
	isPrime=True;
	rangestart= newvalue/2;
	if rangestart%2 == 0:
		rangestart=rangestart-1;
	for i in range(rangestart,2,-2):
		rest = newvalue % i;
		if (rest == 0):		
			isPrime=False;
	if isPrime:
		primcount=primcount+1;
		bigprime=newvalue;	
		newtime=time.clock();
		diff=newtime-oldtime;
		print str(primcount) + "\t" + str(time.clock()) + "\t" + str(diff);
		oldtime=newtime;
		print bigprime;
