
datei = open('13.txt', 'r')
number=1
summe=0
for number in datei.readlines():
	no=int(number)
	summe=summe+no
print summe
result=str(summe)[0:10]
print result
