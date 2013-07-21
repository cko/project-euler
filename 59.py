from string import split

def checkChar(char):
    #if char < 33 or char == ord("}") or char == ord("{") :
    if char == 127 or char < 32 or char == 124 or char == 125 or char == 126 or char == 123:
        return True

def shiftContent(no1, no2, no3, list):
    strResult = ""
    noResult = ""
    orig = ""
    strFile=""
    sum = 0
    for i in range(0, len(list)-1, 3):
        char1 = int(list[i]) ^ no1
        char2 = int(list[i+1]) ^ no2
        char3 = int(list[i+2]) ^ no3
        sum = sum + char1 + char2 + char3
        strResult = strResult + '\t' + chr(char1) + '\t' + chr(char2) + '\t' + chr(char3)
        strFile = strFile + chr(char1) + chr(char2) + chr(char3)
        noResult = noResult + '\t' + str(char1)   + '\t' + str(char2) + '\t'  + str(char3)
        orig = orig + '\t' + list[i]
        if checkChar(char1) or (int(list[0])^ no1)==41 or checkChar(char2) or checkChar(char3):
            return
    
    rest = len(list) % 3
    
    if rest == 0:
        sum=sum+(int(list[len(list)-1])^no1)
    if rest == 1:
        lenl=len(list)
        sum=sum+(int(list[lenl-1]) ^ no1)
    if rest == 2:
        sum=sum+(int(list[len(list)-3])^no1)+(int(list[len(list)-2]) ^ no2) + (int(list[len(list)-1]) ^ no3)
    
    print sum
    datei2 = open('./59_output.txt', 'a')
    datei2.write(str(no1)+' ' + str(no2)+'  ' +str(no3))
    datei2.write(strFile+"\n")
    datei.close()    


datei = open('./59.txt', 'r')
content = datei.read()
list = split(content, ",")


for i in range (80,128):
    for k in range (80,128):
        for l in range(80,128):
            shiftContent(i, k, l, list)
            
shiftContent(103, 111, 100, list)
