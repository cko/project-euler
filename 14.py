

startNumber = 999999
maxCount=0
number=startNumber
while number > 0:
	count=1
	sequence = number;
	while sequence >1:
		if sequence%2 == 0:
			sequence=sequence/2;
			count = count + 1
		else:
			sequence=3*sequence+1
			count=count+1
	number=number-1
	if count > maxCount:
		maxCount=count
		print str(maxCount) +"  " + str(number+1)
