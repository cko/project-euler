def getDivisorSum(n):
	summe = 0
	for i in range(1,n/2+1):
		if n%i==0:
			summe = summe + i
		if summe > n:
			break
	return summe

numberlist =[i for i in range(28123+1)]
abnumbers=set()
for i in range (1,28123+1):
	summe = getDivisorSum(i)
    	if summe > i and i < 28123:
		abnumbers.add(i)

bnumbers=abnumbers.copy()
for number1 in bnumbers:
	print number1
	for number2 in abnumbers:
		number = number1 + number2
		if number in numberlist:
			numberlist.remove(number1+number2)
	abnumbers.remove(number1)

summe=0
for i in numberlist:
	summe=summe+i

print numberlist
print summe
