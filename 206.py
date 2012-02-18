

for i in range(1010101010,1389026625,10):
	result = i * i
	resultStr = str(result)
	#print resultStr
	if resultStr[0]=="1" and resultStr[2]=="2" and resultStr[4]=="3" and resultStr[6]=="4" and resultStr[8]=="5" and resultStr[10]=="6" and resultStr[12]=="7" and resultStr[14]=="8" and resultStr[16]=="9":
		print i		
		print resultStr
