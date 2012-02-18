
product=1
for i in range(1,7830457+1):
	product=product*2
	strpr=str(product)
	if len(strpr) > 12:
		newstr=strpr[1:len(strpr)]
		product= int(newstr)
print product

result=28433*product + 1

print result
	
