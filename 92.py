
result = set()
set_89 = set()

for i in range(1, 10000001):
	current_number = i
	numbers = set()
	in_set_89 = not current_number in set_89
	while not current_number in numbers and in_set_89:
		numbers.add(current_number)
		i_list = list(str(current_number))
		sum = 0
	
		for i_number in i_list:
			i_nu = int(i_number)
			sum += i_nu * i_nu		
		current_number = sum

	if current_number == 89 or current_number in set_89 or 89 in numbers:
		for number in numbers:
			set_89.add(number)
		if i % 200 == 0:
			print len(result)
		result.add(i)

print len(result)