
number = 600851475143L;
biggestd=0;
i=2;

while True:
	i=i+1;	
	if (number % i == 0):
		biggestd=i;
		number=number/i;
	if(number < i):
		break;

print biggestd;
