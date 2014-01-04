def faculty (n):
	value = 1
	while n > 1:
		value = value * n
		n= n-1
	return value	


n = 20
nfaculty = 1


zaehler = faculty(n)
print zaehler

zweinfaculty = faculty(2*n)

result = zweinfaculty / (zaehler * zaehler)

print result


