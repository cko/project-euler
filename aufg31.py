#

def getCoins(amount):
    if amount < 0:
        raise Exception("negative amounts not allowed")
    
    count1 = 1
    count2 = getCount2(amount)
    count5 = getCount5(amount)    
    count10 = getCount10(amount)
    count20 = getCount20(amount)
    count50 = getCount50(amount)
    count100 = getCount100(amount)
    count200 = getCount200(amount)
    print 'amount ' + str(amount)
    return count1 + count2 + count5 + count10 + count20 + count50 + count100 + count200


def getCount200 (amount):
    if amount < 200:
        return 0
    anz = amount / 200
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * 200
        totAnz = totAnz + getCount100(rest) + getCount50(rest) + getCount20(rest) + getCount10(rest) + getCount5(rest) + getCount2(rest) + getCount1(rest)
        if rest == 0:
            totAnz = totAnz + 1
    return totAnz

def getCount100 (amount):
    if amount < 100:
        return 0
    anz = amount / 100
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * 100
        totAnz = totAnz + getCount50(rest) + getCount20(rest) + getCount10(rest) + getCount5(rest) + getCount2(rest) + getCount1(rest)
        if rest == 0:
            totAnz = totAnz + 1
    return totAnz

def getCount50(amount):
    if amount < 50:
        return 0
    anz = amount / 50
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * 50
        totAnz = totAnz + getCount20(rest) + getCount10(rest) + getCount5(rest) + getCount2(rest) + getCount1(rest)
        if rest == 0:
            totAnz = totAnz + 1
    return totAnz

def getCount20(amount):
    if amount < 20:
        return 0
    anz = amount / 20
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * 20
        totAnz = totAnz + getCount10(rest) + getCount5(rest) + getCount2(rest) + getCount1(rest)
        if rest == 0:
            totAnz = totAnz + 1
    return totAnz

def getCount10(amount):
    if amount < 10:
        return 0
    anz = amount / 10
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * 10
        totAnz = totAnz + getCount5(rest) + getCount2(rest) + getCount1(rest)
        if rest == 0:
            totAnz = totAnz + 1
    return totAnz


def getCount5 (amount):
    if amount < 5:
        return 0
    anz = amount / 5
    totAnz = 0
    for i in range(1, anz+1):
        rest = amount - i * 5
        totAnz = totAnz + getCount2(rest) + getCount1(rest)
        if rest == 0:
            totAnz = totAnz + 1
    return totAnz
        
        
def getCount2(amount):
    if amount < 2:
        return 0
    anz = amount / 2
    return anz


def getCount1(amount):
    if amount > 0:
        return 1
    else: 
        return 0


