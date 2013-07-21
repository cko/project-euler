import math

def checkPentagonal (hn):
    squareroot = math.sqrt(1+4*3*2*hn)
    intsqr = int(squareroot)
    if intsqr == squareroot:
        val1 = (1+intsqr)/6.0
        val2 = (1-intsqr)/6.0
        if int(val1)==val1 and val1 > 0:
            return True
        elif int(val2)==val2 and val2 > 0:
            return True
        else:
            return False
    
    
def chechTriangle (hn):
    squareroot = math.sqrt(1+4*2*hn)
    intsqr = int (squareroot)
    if intsqr == squareroot:
        val1 = (-1+intsqr)/2.0
        val2 = (-1-intsqr)/2.0
        if int(val1) == val1 and val1 >0:
            return True
        elif int(val2) == val2 and val2 >0:
            return True
        else:
            return False
        
        
found = False
for i in range (144, 200000):
    hn = i*(2*i-1)
    isPentagonal = checkPentagonal(hn)
    if isPentagonal:
        isTriangle = chechTriangle(hn)
        if isTriangle:
            print hn
            print ''
        
    
    

