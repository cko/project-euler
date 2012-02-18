
count=0
for i in range(1,101):
	jahresziffer=(i+i/4) % 7
	
	rest = 0
	for k in range(0,12):
		montasziffer = 0
		if k==0:
			monatsziffer = 0
			restalt = 0 
			restneu = 31 % 7			
		if k==2 or k==4 or k==6 or k==7 or k==9 or k==11:
			monatsziffer = (restalt + restneu) % 7 
			restalt = monatsziffer
			restneu = 31 % 7 
		if k==3 or k==5 or k==8 or k==10:
			monatsziffer = (restalt + restneu) % 7 
			restalt = monatsziffer
			restneu = 30 % 7
		if k==1:
			monatsziffer = restalt + restneu
			restalt = restneu
			restneu = 28 % 7
		
		schaltjahresziffer = 0
		if i % 4 == 0 and (k == 0 or k == 1):
			schaltjahresziffer = -1

		tagesziffer = 1

		wochentag = (jahresziffer + schaltjahresziffer + tagesziffer + monatsziffer) % 7

		if (wochentag == 0):
			print str(i) + "  " + str(k+1)
			count = count + 1 

print count
