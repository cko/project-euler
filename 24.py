import math
number = "0123456789"
result = ""
#0123456798

rest = 1000000
for i in range(10,0,-1):
	faculty = math.factorial(i)
        count = 0
        if faculty < rest:
		while faculty < rest:
			rest = rest - faculty	
		        count = count + 1
		print count
		print rest
		result = result + number [count:count+1]
		number = number [:count]+number[count+1:]
print "Rest:" + str(rest)	
print result+number


