import math

initial_list = [2,3,5,7]
primes = set(initial_list)
def get_prime_sum ():
	count = 0
	prime_sum = 0
	newvalue = 7
	while count < 11:
		newvalue = newvalue + 2
		isPrime = True;
		rangestart = int(math.ceil(math.sqrt(newvalue))+1)
		if rangestart % 2 == 0:
			rangestart = rangestart-1
		for i in range(rangestart,2,-2):
			rest = newvalue % i
			if (rest == 0):		
				isPrime = False
		if isPrime:
			if is_truncatable_prime(newvalue):
				count = count + 1	
				prime_sum = prime_sum + newvalue
				print newvalue
			primes.add(newvalue)
	return prime_sum


def is_truncatable_prime(prime):
	string_prime = str(prime)
	while len(string_prime) > 1:
		string_prime = string_prime[1:]
		if int(string_prime) not in primes:
			return False
	string_prime2 = str(prime)
	while len(string_prime2) > 1:
		string_prime2 = string_prime2[:-1]
		if int(string_prime2) not in primes:
			return False
	return True
	

prime_sum = get_prime_sum()
print "-----------"
print prime_sum

