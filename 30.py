import math
ergebnis=0
for i in range (2,2000000):
	zahl = str(i)
	summe = 0 
	for k in range(0,len(zahl)):
		summe = summe + math.pow(int(zahl[k]),5)
	if summe == i:
		ergebnis=ergebnis+int(zahl)

print ergebnis
