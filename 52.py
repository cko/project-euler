import math 

def contain_same_digits (number1, number2):
	string1 = str(number1)
        string2 = str(number2)
	new_string1 = sorted(string1)
	new_string2 = sorted(string2)
	return new_string1 == new_string2

def find_number(min_value, max_value):
	for number in range(min_value, max_value):
		if not contain_same_digits (number, number * 2):
			continue
		if not contain_same_digits (number, number * 3):
			continue
		if not contain_same_digits (number, number * 4):
			continue
		if not contain_same_digits (number, number * 5):
			continue
		if contain_same_digits (number, number * 6):
			return number
	return -1


p = 0
while p < 8:
	min_value = long(math.pow(10, p))
	max_value = long(min_value * 5/3) + 1
	
	result_number = find_number (min_value, max_value)
	if result_number != -1:
		print result_number
		break
	else:	
		p = p + 1
