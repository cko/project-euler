def read_triangles_from_file ():
	triangles = []
	with open('triangles.txt', 'r') as f:
		for line in f:
			triangle = line.rstrip('\n')
			triangles.append(triangle)
	return triangles

def get_A(line):
	values = line.split(',')
	values = map(float, values)
	A = []
	A.append([values[0], values[2], values[4]])
	A.append([values[1], values[3], values[5]])
	A.append([1,1,1])
	return A

def get_L_and_R (A):
	R = list(A)
	L = [[0,0,0], [0,0,0],[0,0,0]]	
	for spalte in range(0,3):
		L[spalte][spalte] = 1
		for zeile in range(spalte+1,3):
			quotient = float(R[zeile][spalte]/R[spalte][spalte])
			L[zeile][spalte] = quotient
			for position in range (0,3):
				R[zeile][position] = R[zeile][position] - quotient * R[spalte][position]
	return L,R

def get_results (L,R,b):
	y_1 = b[0]
	y_2 = b[1] - L[1][0] * y_1
	y_3 = b[2] - L[2][0] * y_1 - L[2][1] * y_2
	x_3 = y_3 / R[2][2]
	x_2 = (y_2 - R[1][2] * x_3) / R[1][1]
	x_1 = (y_1 - R[0][2] * x_3 - R[0][1] * x_2) / R[0][0]
	return x_1, x_2, x_3

triangles = read_triangles_from_file()
count_inside = 0

for triangle in triangles:
	A = get_A (triangle)
	b = [0,0,1]
	L,R = get_L_and_R(A)
	x_1, x_2, x_3 = get_results(L,R,b)
	if x_1 > 0 and x_1<1:
		if x_2 > 0 and x_2 < 1:
			if x_3 > 0 and x_3 < 1:
				count_inside += 1
print count_inside