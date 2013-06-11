peters_possible_values = {}
colins_possible_values = {}
for i in range(9, 37):
	peters_possible_values[i] = 0
for i in range(6, 37):
	colins_possible_values[i] = 0

def calc_peters_possible_values (sum, count):
	if count == 9:
		value = peters_possible_values[sum]
		peters_possible_values[sum] = value + 1
	elif count < 9:
		calc_peters_possible_values(sum + 1, count + 1)
		calc_peters_possible_values(sum + 2, count + 1)
		calc_peters_possible_values(sum + 3, count + 1)
		calc_peters_possible_values(sum + 4, count + 1)

def calc_colins_possible_values (sum, count):
	if count == 6:
		value = colins_possible_values[sum]
		colins_possible_values[sum] = value + 1
	elif count < 6:
		calc_colins_possible_values(sum + 1, count + 1)
		calc_colins_possible_values(sum + 2, count + 1)
		calc_colins_possible_values(sum + 3, count + 1)
		calc_colins_possible_values(sum + 4, count + 1)
		calc_colins_possible_values(sum + 5, count + 1)
		calc_colins_possible_values(sum + 6, count + 1)


calc_peters_possible_values(0,0)
for k, v in peters_possible_values.iteritems():
        peters_possible_values[k] = float (peters_possible_values[k])/262144
calc_colins_possible_values(0,0)
for k, v in colins_possible_values.iteritems():
        colins_possible_values[k] = float (colins_possible_values[k])/46656

prob = 0.0
for k_p, v_p in peters_possible_values.iteritems():
	for k_c, v_c in colins_possible_values.iteritems():
		if k_p > k_c:
			prob += v_p * v_c

print prob