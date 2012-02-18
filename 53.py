

def select_r_from_n (n, r):
	result = 1	
	for i in range (r+1, n+1):
		result = result * i
	for i in range(1, n-r+1):
		result = result / i;
	return result;


count = 0
for n in range(10,101):
	for r in range(3, n - 1):
		value = select_r_from_n(n,r)
		print str(n) + ' ' + str(r) + ' ' + str(value)		
		if value > 1000000:
			count = count + 1
print count
