

result = 1;
factors=[];

for i in range (1,20):
	if result % i != 0:
		factor=i;
		for n in factors:
			if factor % n == 0:
				factor = factor / n;
		result = result * factor;
		factors.append(factor)
		print i;
		print result; 

for i in range (1,20):
	print result/i;

print result;
