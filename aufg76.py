
def getNumber(amount):
    if amount < 0:
        raise Exception("negative amounts not allowed")
    
    count1 = 1
    count = 0
    for i in range(99, 1, -1):
        count = count + getCount(amount, i)
        print str(i) + '   ' + str(count)
    return count1 + count

def getCount (amount, muenz):
    if amount < muenz:
        return 0
    anz = amount / muenz
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * muenz
        for k in range (2, muenz):
            totAnz = totAnz + getCount(rest, k) 
        totAnz = totAnz + 1
    return totAnz
