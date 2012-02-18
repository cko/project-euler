
class Fifteen:
	
    def __init__(self, verbose=0):
	self.count = 0


    def lab(self,xlength,ylength):

	if xlength > 0 and ylength >0:		
		self.lab (xlength - 1, ylength)
		self.lab (xlength, ylength -1)
	if xlength==0 or ylength==0:
		self.count = self.count + 1;
		print str(xlength) + ' ' + str(ylength) + ' ' + str(self.count)
		
	

    def getCount (self):
	return self.count


fifteen = Fifteen ();
fifteen.lab(20,20);
print fifteen.count
