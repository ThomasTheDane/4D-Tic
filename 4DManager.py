import bigBoard
import smallBoard

class small_board():
	def __init__(self):
		self.smallBoardList = ["X" for i in range(9)]
		
class big_board(): #tic-tac-toe board object
	def __init__(self):
		self.bigBoardList = [small_board() for i in range(9)]
		
	#prints out the board
	def print_board(self):
		print("#########################")
		print("#       #       #       #")

		for m in range(0,9,3):
			for k in range(0, 9, 3):
				toPrintString = "# "
				for i in range(0, 3):
					for j in range(0,3):
						toPrintString += self.bigBoardList[i+m].smallBoardList[j+k]
						if(j != 2):
							toPrintString += "|"
						else:
							toPrintString += " # "
							
				print(toPrintString)
			if(m != 6):
				print("#       #       #       #")
				print("#########################")
				print("#       #       #       #")
		print("#       #       #       #")
		print("#########################")
		
class aGame():
	def __init__(self):
		theBigBoard = big_board()
	def getPlayers(self):
		isValidInput = False
		while(not isValidInput):
			try:
				self.numPlayers = input("Number of Players: ")
				self.playersSymbol = []
				self.numPlayers = int(self.numPlayers)
				isValidInput = True
			except:
				isValidInput = False

		for i in range(0, self.numPlayers):
			isValidInput = False
			while(not isValidInput):
				inputAsk = "Player number " + str(i+1) + " symbol is : "
				self.playersSymbol += input(inputAsk)
				if(len(self.playersSymbol[i]) == 1 and not(self.playersSymbol[i] in self.playersSymbol[:-1])):
					isValidInput = True
				else:
					self.playersSymbol.pop()

					
	def printPlayers(self):
		for i in range(0, self.numPlayers):
			print("Player " + str(i + 1) + " is symbol " + self.playersSymbol[i])

	def startGame(self):
		self.getPlayers()
		
theGame = aGame()
theGame.startGame()
theGame.printPlayers()

