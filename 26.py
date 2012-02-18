from decimal import Decimal
import decimal



def process_number(num, original):
	character1 = num[5:7]
        num2 = num.replace(character1,'')
        if len(num2) > 7:
		seq1 = num[3:10]
		position = num.find(seq1, 10)
		global maxdist
		global value
		if position > maxdist:
			maxdist = position
			value = original


maxdist = 0
value = 0

for i in range(1, 1000):
	decimal.getcontext().prec = 1500
        dec = Decimal(1.0)/Decimal(i)
	decstr = str(dec)
	if len(decstr) > 10:
		process_number(decstr[2:], i)
print 'distance: ' + str(maxdist)
print 'number: ' + str(value)
print Decimal(1.0)/Decimal(value)
print '\n'
        
