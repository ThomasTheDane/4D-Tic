#class textbox takes 4 paramters and can print text box
class textBox():
	#initializes the box
	def __init__(self,width, height, fill, edge):
		self.width = width
		self.height = height
		self.fill = fill
		self.edge = edge
	#prints the box using parameters
	def printBox(self):
		print(self.width * self.edge)
		for i in range(0, self.height-2):
			print(self.edge + ((self.width -2) * self.fill) + self.edge)
		print(self.width * self.edge)
	
#For testing class text box, only called when executed directly
if(__name__=="__main__"):
	#instantiates a box and prints it
	aBox = textBox(4,5,'+','#')
	aBox.printBox()
	
#notes for assignment:
#=====================
#Changes I made included making it into a class, increasing modularity of the program
#Also uses the much more efficient string manipulation and creation methods 
#Also commented it, not too much, not too little