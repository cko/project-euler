
def findPalindromicNumbersBase10 ():
	numbers = set()
	for i in range(1, 1000000):
		number = str(i)
		length = len(number) / 2
		part1 = number[0:length]
		if len(number) % 2 == 0:
			part2number = number[length:]
		else:
			part2number = number[length+1:]
		part2 = part2number[::-1]
		if part1==part2:
			#print i	
			numbers.add(i)
	return numbers


def findPalindromicNumbersBase2(base10):
	summe=0
	for i in base10:
		number = dec2bin(i)
		length = len(number) / 2
		part1 = number[0:length]
		if len(number) % 2 == 0:
			part2number = number[length:]
		else:
			part2number = number[length+1:]
		part2 = part2number[::-1]
		if part1==part2:
			summe = summe + i
	print summe


def dec2bin(n):
	s = ''
	while n:
		s = str(n % 2) + s
		n = n / 2
	return s

numbers = findPalindromicNumbersBase10()
findPalindromicNumbersBase2(numbers)
