total = 0

def rounds ():
	numbers1 = set([0,1,2,3,4,5,6,7,8,9])
	for number1 in numbers1:
		numbers2 = set(numbers1)
		numbers2.remove(number1)
		for number2 in numbers2:
			calculate_number3_upwards(number1, number2, numbers2);


def calculate_number3_upwards (number1, number2, numbers2):
	numbers3 = set(numbers2)
	numbers3.remove(number2)
	for number3 in numbers3:
		numbers4 = set(numbers3)
		numbers4.remove(number3)
		for number4 in numbers4:
			if number4 % 2 == 0:
				str_1_2 = str(number1) + str(number2)
				calculate_number5_upwards(str_1_2, number3, number4, numbers4)
				

def calculate_number5_upwards (str_1_2, number3, number4, numbers4):
	numbers5 = set(numbers4)
	numbers5.remove(number4)
	#print str_1_2
	for number5 in numbers5:
		str_3_4_5 = str(number3)+str(number4)+str(number5)
		n_3_4_5 = int(str_3_4_5)
		if n_3_4_5 % 3 == 0:
			numbers6 = set(numbers5)
			numbers6.remove(number5)
			for number6 in numbers6:
				str_4_5_6 = str(number4)+str(number5)+str(number6)
				n_4_5_6 = int(str_4_5_6)
				if n_4_5_6 % 5 == 0:
					str_1_2_3_4 = str_1_2 + str(number3) + str(number4)
					calculate_number7_upwards (str_1_2_3_4, number5, number6, numbers6)


def calculate_number7_upwards (str_1_2_3_4, number5, number6, numbers6):
	numbers7 = set(numbers6)
	numbers7.remove(number6)
	for number7 in numbers7:
		str_5_6_7 = str(number5)+str(number6)+str(number7)
		n_5_6_7 = int(str_5_6_7)
		if n_5_6_7 % 7 == 0:
			numbers8 = set(numbers7)
			numbers8.remove(number7)
			for number8 in numbers8:
				str_6_7_8 = str(number6)+str(number7)+str(number8)
				n_6_7_8 = int(str_6_7_8)
				if n_6_7_8 % 11 == 0:
					str_1_2_3_4_5_6 = str_1_2_3_4 + str(number5) + str(number6)
					calculate_number9_upwards (str_1_2_3_4_5_6, number7, number8, numbers8)


def calculate_number9_upwards(str_1_2_3_4_5_6, number7, number8, numbers8):
	numbers9 = set(numbers8)
	numbers9.remove(number8)
	for number9 in numbers9:
		str_7_8_9 = str(number7)+str(number8)+str(number9)
		n_7_8_9 = int(str_7_8_9)
		if n_7_8_9 % 13 == 0:
			numbers10 = set(numbers9)
			numbers10.remove(number9)
			for number10 in numbers10:
				str_8_9_10 = str(number8)+str(number9)+str(number10)
				n_8_9_10 = int(str_8_9_10)
				if n_8_9_10 % 17 == 0:
					n = str_1_2_3_4_5_6 + str(number7) + str(number8) + str(number9) + str(number10)
					global total
					total += int(n)


rounds()
print total