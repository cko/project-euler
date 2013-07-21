

resultSet=set()

for i in range(1, 10000):
    for k in range (1, i):
        result = i * k
        resultStr = str(i) + " " + str(k) + " " + str(result)
        if len(resultStr) == 11 and resultStr.find("1") > -1 and resultStr.find("2") > -1 and resultStr.find("3") > -1 and resultStr.find("4") > -1 and resultStr.find("5") > -1 and resultStr.find("6") > -1 and resultStr.find("7") > -1 and resultStr.find("8") > -1 and resultStr.find("9") > -1:
            print resultStr
            resultSet.add(result)
        if len(resultStr) > 11:
                #print "ill:" + resultStr
                break
            
print resultSet

print sum(resultSet)
