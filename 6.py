
squareofsum= (100*(100+1)/2)*(100*(100+1)/2);
print squareofsum;
sumofsquares=0;

for i in range (1,101):
	sumofsquares = sumofsquares + i*i;
	print sumofsquares;
print squareofsum-sumofsquares;
