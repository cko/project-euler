
class eighteen:

	def __init__(self):
		self.a = [None]*15
		self.a [0] = [75]
		self.a [1] = [95, 64]
		self.a [2] = [17, 47, 82]
		self.a [3] = [18, 35, 87, 10]
		self.a [4] = [20, 04, 82, 47, 65]
		self.a [5] = [19, 01, 23, 75, 03, 34]
		self.a [6] = [88, 02, 77, 73, 07, 63, 67]
		self.a [7] = [99, 65, 04, 28, 06, 16, 70, 92]
		self.a [8] = [41, 41, 26, 56, 83, 40, 80, 70, 33]
		self.a [9] = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
		self.a [10] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
		self.a [11] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
		self.a [12] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
		self.a [13] = [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
		self.a [14] = [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
		self.maxsum=0

	def calculate (self, i,k,sumn):
		sumn=sumn+self.a[i][k]
		if i<14:
			self.calculate(i+1,k,sumn)
			self.calculate(i+1,k+1,sumn)
		else:
			if sumn > self.maxsum:
				self.maxsum=sumn
	def getmaxsum (self):
		return self.maxsum

instance = eighteen()	
instance.calculate(0,0,0)
print instance.getmaxsum()


