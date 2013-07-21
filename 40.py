

numberStr = ''

for i in range(1,200000):
    numberStr = numberStr + str(i)
    
no1= int(numberStr[0])
no2= int(numberStr[9])
no3= int(numberStr[99])
no4= int(numberStr[999])
no5= int(numberStr[9999])
no6= int(numberStr[99999])
no7= int(numberStr[999999])

print str(no1*no2*no3*no4*no5*no6*no7)