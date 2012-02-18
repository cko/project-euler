import math


result=set()
for i in range(2,101):
	for k in range(2,101):
		result.add(math.pow(i,k))

print len(result)
