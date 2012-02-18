import time
import math

newvalue=3
primes = set(("1", "3"))
while newvalue<1000000L:
	newvalue = newvalue + 2
	isPrime=True
	rangestart= int(math.ceil(math.sqrt(newvalue))+1)
	if rangestart%2 == 0:
		rangestart=rangestart-1
	for i in range(rangestart,2,-2):
		rest = newvalue % i
		if (rest == 0):		
			isPrime=False
	if isPrime:
		primes.add(str(newvalue))

count = 0
for prime in primess:
  	newprime = prime
	is_circulare_prime = True
	for i in range(0, len(prime)): 
                newprime = newprime[1:] + newprime[:1]
		if newprime not in primes:
			is_circulare_prime = False
			break
	if is_circulare_prime:
		count = count + 1
		print prime
print "Count: " + str(count)
