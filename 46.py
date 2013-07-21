from math_lib import is_prime
import math

primes = set()
primes.add(2)


def check_number (number):
	if is_prime (number):
		primes.add(number)
		return
	else:
		is_composite = False
		for prime in primes:
			remainder = number - prime
			remainder = remainder / 2
			r_sqrt = math.sqrt(remainder)
			if int(r_sqrt) * int(r_sqrt) == remainder:
				is_composite = True
        if not is_composite:
            print number		

for i in range(3,10000,2):
	check_number(i)
