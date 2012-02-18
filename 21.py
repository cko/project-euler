import math

def calculateDivSum(i):
	a=[]	
	for d in range (i/2+1,0,-1):
		if i%d == 0:
			a.append(d)
	summ=0	
	for k in range(0,len(a)):
		summ=summ+a[k]
	return summ

totalSum=0
myset=set()
for i in range(0,10000,2):
	newNumber = calculateDivSum(i)
	if i==calculateDivSum(newNumber) and i != newNumber:
		if newNumber not in myset:
			myset.add(i)
			myset.add(newNumber)

for number in myset:
	totalSum=totalSum+number
print totalSum
