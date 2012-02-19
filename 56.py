import math

def calculate_digital_sum (number):
	digit_sum = 0
	string1 = str("%0d" % number)
	for c in string1:
		digit_sum = digit_sum + int(c)
	return digit_sum

max_sum = -1
for a in range (20, 100):
	for b in range (10,100):
		number = a ** b	
		digital_sum = calculate_digital_sum (number)
		if digital_sum > max_sum:
			max_sum = digital_sum

print max_sum
