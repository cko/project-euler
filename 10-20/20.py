
faculty=1
for i in range(100,1,-1):
	faculty= faculty * i;
print faculty

facultyStr=str(faculty)
summe=0
for i in range (0,len(facultyStr)):
	summe = summe + int(facultyStr[i])
print summe
	
