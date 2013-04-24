import bigBoard
import smallBoard

class small_board():
	def __init__(self):
		self.smallBoardList = [" " for i in range(9)]
		
class big_board(): #tic-tac-toe board object
	def __init__(self):
		self.bigBoardList = [small_board() for i in range(9)]
		
	def receiveInput(self, bigIndex, smallIndex, symbolInput):
		self.bigBoardList[bigIndex-1].smallBoardList[smallIndex-1] = symbolInput
	
	def getSpotSymbol(self, bigIndex, smallIndex):
		return self.bigBoardList[bigIndex-1].smallBoardList[smallIndex-1]
	
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
		self.theBigBoard = big_board()
	
	def getPlayersSymbol(self):
		isValidInput = False
		self.playersSymbol = []
		for i in range(0, self.numPlayers):
			isValidInput = False
			while(not isValidInput):
				inputAsk = "Player number " + str(i+1) + " symbol is : "
				self.playersSymbol += input(inputAsk)
				if(len(self.playersSymbol[i]) == 1 and not(self.playersSymbol[i] in self.playersSymbol[:-1]) and self.playersSymbol[i] != " "):
					isValidInput = True
				else:
					self.playersSymbol.pop()

					
	def printPlayers(self):
		for i in range(0, self.numPlayers):
			print("Player " + str(i + 1) + " is symbol " + self.playersSymbol[i])

	def askForInput(self):
			isValidMove = False			
			while(not isValidMove):
				try:
					tryMove = input("where would you like to place " + self.playersSymbol[self.currentTurn] + " : ")
					bigIndexMove = int(tryMove[0])
					smallIndexMove = int(tryMove[2])
					if(bigIndexMove == 0 or bigIndexMove > 9):
						raise ValueError
					if(self.theBigBoard.getSpotSymbol(bigIndexMove, smallIndexMove) != " "):
						raise ValueError
					isValidMove = True
				except:
					print("Please input location in format {big board spot,small board spot} with some where that isn't taken")
					isValidMove = False
			
			self.theBigBoard.receiveInput(bigIndexMove,smallIndexMove, self.playersSymbol[self.currentTurn])
			
	def startGame(self):
		self.currentTurn = 0
		self.getPlayerTypes()
		self.getPlayersSymbol()
		
	def showBoard(self):
		self.theBigBoard.print_board()
	
	def nextTurn(self):
		self.showBoard()
		if(self.playersType[self.currentTurn] == 'Human'):
			self.askForInput()
		elif(self.playersType[self.currentTurn] == 'AI'):
			self.makeAIMove()
		elif(self.playersType[self.currentTurn] == 'Monkey'):
			self.makeMonkeyMove()
		else:
			print('Critical Mission Failure #1')
		
	def makeAIMove(self):
		makeMonkeyMove()

	def makeMonkeyMove(self):
		pass
		
	def playTheGame(self):
		self.gameIsGoing = True
		while(self.gameIsGoing):
			self.nextTurn()
			self.currentTurn += 1
			if(self.currentTurn == self.numPlayers):
				self.currentTurn = 0
	
	def getPlayerTypes(self):
		isValidInput = False
		self.playersType = []
		while(not isValidInput):
			try:
				self.numPlayers = input("Number of Players: ")
				self.numPlayers = int(self.numPlayers)
				isValidInput = True
			except ValueError:
				isValidInput = False

		for i in range(0, self.numPlayers):
			isValidInput = False
			while(not isValidInput):
				inputAsk = "Player number " + str(i+1) + " type is (Monkey, AI, Human): "
				strInput = input(inputAsk)
				strInput = str(strInput)
				if(strInput == 'Monkey' or strInput == 'AI' or strInput == 'Human'):
					isValidInput = True
					self.playersType += [strInput]
				
			
theGame = aGame()
theGame.startGame()
#theGame.playTheGame()
