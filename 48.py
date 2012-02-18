import math

summe=0L;
for i in range(1,1001):
	zwischenprodukt = i;
	for k in range(i-1,0,-1):
		zwischenprodukt = zwischenprodukt * i;
	#print 'Zwischenprodukt: '+ str(i) + '  '  + str(zwischenprodukt)
	summe = summe + zwischenprodukt;

print summe

