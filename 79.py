import sys

def getFromEnd(lines,zifferncopy):
	for line in lines:
		if int(line[0]) in zifferncopy:
			zifferncopy.remove(int(line[0]))
		if len(line) > 1 and int(line[1]) in zifferncopy:
			zifferncopy.remove(int(line[1]))
	if len(zifferncopy)==1:
		return zifferncopy.pop()
	else:
		raise Exception ("no number found") 


def getFromStart(lines,zifferncopy):
	for line in lines:
		if len(line) >2 and int(line[2]) in zifferncopy:
			zifferncopy.remove(int(line[2]))
		if len(line) > 1 and int(line[1]) in zifferncopy:
			zifferncopy.remove(int(line[1]))
	if len(zifferncopy)==1:
		return zifferncopy.pop()
	else:
		raise Exception ("no number found") 


	
def removeFromEnd(number, zahlen):
	subset=set()
	for zahl in zahlen:
		if zahl[len(zahl)-1] == str(number):
			subset.add(zahl)

	for zahl in subset:
		zahlen.remove(zahl)
		if len(zahl) > 1:
			zahlen.add(zahl[0:len(zahl)-1])


def removeFromStart(number, zahlen):
	subset=set()
	for zahl in zahlen:
		if len(zahl) > 0 and zahl[0] == str(number):
			subset.add(zahl)

	for zahl in subset:
		zahlen.remove(zahl)
		if len(zahl)>1:
			zahlen.add(zahl[1:len(zahl)])


datei = open('79.txt', 'r')
lines = datei.readlines()
zahlen=set()
ziffern=set()
for line in lines:
	zahlen.add(line[0:3])
	ziffern.add(int(line[0]))
	ziffern.add(int(line[1]))
	ziffern.add(int(line[2]))

count=len(ziffern)
resultEnd=""
resultStart=""


while len(resultEnd+resultStart) < count:
	try:
		zifferncopy=ziffern.copy()
		number = getFromEnd(zahlen,zifferncopy)
		removeFromEnd(number,zahlen)
		ziffern.remove(number)
		resultEnd = str(number) + resultEnd
	except Exception:
		zifferncopy=ziffern.copy()
		number = getFromStart(zahlen,zifferncopy)
		removeFromStart(number,zahlen)
		ziffern.remove(number)
		resultStart = resultStart + str(number)		

print resultStart+resultEnd	
