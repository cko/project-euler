

for i in range(999,630,-1):
	for k in range(i-1,630,-1):
		result=i*k;		
		nstring = str(result);
		string1=nstring[0:3];
		string2=nstring[3:];
		string2rev=string2[::-1];
		if string1 == string2rev:
			print result;
