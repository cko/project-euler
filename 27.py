import math

def get_value_quadratic_formula (a, b, n):
	return n * n + a * n + b;

def is_prime (zahl):
	if zahl < 0:
		return False
	is_prime = True
	rangestart= int(math.ceil(math.sqrt(zahl))+1)
	if rangestart%2 == 0:
		rangestart=rangestart-1
	for i in range(rangestart,2,-2):
		rest = zahl % i
		if (rest == 0):		
			is_prime=False
	return is_prime

n_max = -1
a_max = -1
b_max = -1
for a in range(-1000, 1000):
	for b in range (-1000, 1000):
		n = 0;
		while True:
			value = get_value_quadratic_formula (a, b, n)
			if is_prime (value):
				n = n + 1
			else:
				break
		if n > n_max:
			n_max = n
			a_max = a
			b_max = b

print "a: " + str(a_max) + "  b: " + str(b_max) + "  n: " + str(n_max)
print a_max * b_max
