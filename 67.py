
datei = open('/home/ck/Desktop/triangle.txt','r')
oldline = [0,0]
for zeile in datei.readlines():
     newline = zeile.split(' ')
     newvalues = [0] * len(newline)
     for i in range(0, len(newline)):
        if i == 0:
		oldvalue = oldline[i]
        elif i == len(oldline):
		oldvalue = oldline[len(oldline)-1]
        else:
       		oldvalue = max(oldline[i], oldline[i-1])
        newvalues [i] = oldvalue + int(newline [i])
     oldline = newvalues
     print oldline
print max(newvalues)
