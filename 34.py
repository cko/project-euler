


def calculateFaculty(n):
    result=1
    for i in range(2,n+1):
        result = result * i
    return result

totalsum=0
for i in range (3,1000000):
    number = str(i)
    sum = 0
    for k in range (len(number)):
        digit = int(number[k])
        sum = sum + calculateFaculty(digit)
        
    if i == sum:
        print i
        print ''   
        totalsum = totalsum + sum
    
print 'Totalsum: ' + str(totalsum)
    
