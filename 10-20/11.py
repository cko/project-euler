
datei = open('11.txt', 'r')
numbers=[]
for line in datei.readlines():
	numbers.append(line.split())
	
#zeilen
maxprodukt=0
for i in range(0,20):
	for k in range(0,20-3):
		produkt= int(numbers[i][k])*int(numbers[i][k+1])*int(numbers[i][k+2])*int(numbers[i][k+3])
		if produkt > maxprodukt:
			maxprodukt=produkt


#spalten
for i in range(0,20):
	for k in range(0,20-3):
		produkt= int(numbers[k][i])*int(numbers[k+1][i])*int(numbers[k+2][i])*int(numbers[k+3][i])	
		if produkt > maxprodukt:
			maxprodukt=produkt

#diagonal links oben nach rechts unten
for i in range(0,20-3):
	for k in range(0,20-3):
		produkt= int(numbers[k][i])*int(numbers[k+1][i+1])*int(numbers[k+2][i+2])*int(numbers[k+3][i+3])	
		if produkt > maxprodukt:
			maxprodukt=produkt

#diagonal links unten nach rechts oben
for i in range(0,20-3):
	for k in range(0,20-3):
		produkt= int(numbers[i+3][k])*int(numbers[i+2][k+1])*int(numbers[i+1][k+2])*int(numbers[i][k+3])
		print numbers[i+3][k] + " " + numbers[i+2][k+1] + " " + numbers[i+1][k+2] + " " + numbers[i][k+3]
		if produkt > maxprodukt:
			maxprodukt=produkt

print maxprodukt
