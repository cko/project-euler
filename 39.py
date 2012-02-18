import math
import operator

result = {}
for a in range (1, 999):
	for b in range (1, 999):
		c_square = a * a + b * b
		c = math.sqrt (c_square)
		if c.is_integer():
			summe = a + b+ int (c)
			if summe <= 1000:
				if summe in result:
					result[summe] = result[summe] + 1
				else:
					result[summe] = 1
newlist = sorted(result.iteritems(), key=operator.itemgetter(1))
print newlist[-1]
