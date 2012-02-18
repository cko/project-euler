
fn1=1
fn2=1
fneu=0;
count=2;
while len(str(fneu))<1000:
	fneu=fn1+fn2;
	count=count+1;
	fn2=fn1;
	fn1=fneu;
	print count;
