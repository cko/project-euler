import math

def reverseNumber (number1):
	s = str(number1)
        reverse = s[::-1]
	return long(reverse)

def is_palindrome (result_number):
	if result_number < 10:
		return True
	result = str(result_number)	
	length = len (result)
	first_half = result [:length/2]
	index = int(math.ceil(length/2.0))
	second_half = result [index:]
	return first_half == second_half[::-1]

def search_palindrome (number1, number2):
	result = long(number1 + number2)
	for i in range (1,51):	
		palindrom = is_palindrome (result)
		if (palindrom):
			return True
		else:
			result2 = result + reverseNumber(result)
			result = result2
	return False

count = 0
for i in range(1, 10000):
	number2 = reverseNumber(i)
	if search_palindrome(i, number2):
		count = count + 1
print 9999 - count
	
