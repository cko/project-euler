def read_matrix_from_file ():
	matrix = []
	with open('matrix.txt', 'r') as f:
		for line in f:
			row = line.rstrip('\n')
			values = line.split(',')
			values = map(int, values)
			matrix.append(values)
	return matrix

def find_min_value (matrix):
	size = 80
	values = [[100000] * size for i in range(size)]
	for row in range(0,size):
		for column in range(0,size):
			if row == 0 and column == 0:
				values[0][0] = matrix[row][column]
			elif row == 0:
				values[0][column] = matrix[0][column] + values[0][column-1]
			elif column == 0:
				values[row][0] = matrix[row][0] + values[row-1][0]
			else:
				prev_col = values[row][column - 1]
				prev_row = values[row-1][column]
				min_prev = min([prev_row, prev_col])
				values[row][column] = matrix[row][column] + min_prev
	return values[size-1][size-1]

matrix = read_matrix_from_file()
min_value = find_min_value(matrix)
print min_value