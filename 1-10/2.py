
vorgaenger=1;
vorvorgaenger=1;
fibonacci=0;
result=0;

while True:
	fibonacci = vorgaenger + vorvorgaenger;
        if fibonacci > 4000000L:
		break;
	vorvorgaenger=vorgaenger;
	vorgaenger=fibonacci;
	if fibonacci % 2 == 0:
		result+=fibonacci

print result;
