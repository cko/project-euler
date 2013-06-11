import math

def is_triangle(d1,d2,d3):
	d_list = [d1,d2,d3]
	d_list.sort()
	
	if d_list[0] == 0 or d_list[1] == 0 or d_list[2] == 0:
		return False
	if d_list[0] + d_list[1] == d_list[2]:
		return True

def get_number_triangles():
	count = 0
	size = 51
	for x_1 in range(0,size):
		print x_1
		for y_1 in range(0,size):
			if not x_1 == 0 or not y_1 == 0: 
				d_origin_1 = x_1*x_1 + y_1*y_1
				for x_2 in range(0,size):
					for y_2 in range(0,size):
						d_origin_2 = x_2*x_2 + y_2*y_2
						d_1_2 = (x_1-x_2)*(x_1-x_2) + (y_1 - y_2)*(y_1 - y_2)
						if is_triangle(d_origin_1, d_origin_2, d_1_2):
							count += 1
	return count

print get_number_triangles()/2

