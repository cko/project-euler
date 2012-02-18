def getSumDigits (n):
	counts=[3,3,5,4,4,3,5,5,4]
	sumdigits=0	
	for i in range(0, n):
		sumdigits=sumdigits+counts[i]
	return sumdigits	



n=1000
#ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen
counts=[3,6,6,8,8,7,7,9,8,8]
countsdigits=[3,3,5,4,4,3,5,5,4]


sumdigits=getSumDigits(9)*9*10

#summe 1-9
msum=sumdigits


# summe 10-19
oddsum=0
for i in range(0, 10 ):
	oddsum=oddsum+counts[i-1]
oddsum = oddsum * 10
msum = msum + oddsum

#summe 20-99 - twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety
countsdecimals=[6,6,5,5,5,7,6,6]
sumd=0
for i in range(0,8):
	sumd=sumd + 10*10*countsdecimals[i]

msum=msum+sumd



#summe 100-999
#hundred=7
#and=3
sumhundreds=0
for i in range(0,9):
	sumhundreds=sumhundreds+ (countsdigits[i] + 7) * 100
	sumhundreds=sumhundreds+ 3*99
msum=msum+sumhundreds
		


##thousand=8
msum=msum+3+8
print str(msum)

