import math

result = 2L
for i in range(1,1000):
	result=result*2L
print result

#rest=result
#summe=0L
#while rest > 0:
#	summe = summe + rest % 10
#	print "Modulo: " + str(rest%10)
#	rest= math.floor(rest/10)
#	print rest
#print summe

summe=0
resultStr = str (result)
for i in range(0,len(resultStr)):
	summe = summe + int(resultStr[i])
print summe
