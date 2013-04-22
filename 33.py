from math_lib import euclid

def do_euclid (i, j):
	count = 0
	gcd = i
	old_i = i
	old_j = j
	while gcd > 1:
		gcd = euclid(i, j)
		if gcd > 1:
			count += 1
			i = i / gcd
			j = j / gcd
	if count > 0:
		check_for_curious_values (old_i, old_j, i, j)


def check_for_curious_values (old_i, old_j, i, j):
	for k in range (1, old_i/i):
		str_old_i = str(old_i)
		str_i = str(i * k)
		str_old_j = str(old_j)
		str_j = str(j*k)
		if check_numbers(str_i, str_old_i, str_j, str_old_j):
			print str_old_j + '/' + str_old_i + '    ' + str_j + '/' + str_i
			break


def check_numbers (str_i, str_old_i, str_j, str_old_j):
	if str_old_i[1] == str_i:
		if str_old_j[0] == str_j:
			if str_old_j[1] == str_old_i[0]:
				return True
	return False


for i in range(10,100):
	for j in range(10, i):
		if i != j:
			str_i = str(i)
			str_j = str(j)
			if str_i[0] in str_j or str_i[1] in str_j:
				do_euclid(i,j)			