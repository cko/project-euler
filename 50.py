import math

def get_primes ():
	bigprim = 3
	newvalue = 3
	primes = [1,2,3]
	while True:
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
			bigprim = newvalue	
			if bigprim > 1000000L:
				break
			primes.append(bigprim)
	return primes


def get_longest_sum_prime(primes):
	max_count = 0
	max_prime = 0
	prime_set = set(primes)
	i = len(primes)-1
	for l in range(0,(i-1)/5,1):
		prime_sum = 0
		count = 0
		for k in range(l,i-1,1):
			prime_sum = prime_sum + primes [k]
			count = count + 1

			if prime_sum in prime_set:
				if count >= max_count:
					max_count = count
					max_prime = prime_sum
			elif prime_sum > primes [i]:
				break
	return max_prime

primes = get_primes()
prime = get_longest_sum_prime(primes)
print prime

