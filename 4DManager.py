import bigBoard
import smallBoard

win_combos =([0, 1, 2],
			 [3, 4, 5], 
			 [6, 7, 8],
			 [0, 3, 6], 
			 [1, 4, 7], 
			 [2, 5, 8],
			 [0, 4, 8],
			 [2, 4, 6]) #All possible winning combinations


class small_board():
	def __init__(self,posList=0):
		if posList == 0:
			self.smallBoardList = [" " for i in range(9)]
		else:
			self.smallBoardList = posList

	def check_win_p(self):
		for win_line in win_combos:
			if self.smallBoardList[win_line[0]] != " " and self.smallBoardList[win_line[0]] == self.smallBoardList[win_line[1]] and self.smallBoardList[win_line[1]] == self.smallBoardList[win_line[2]]:
				return self.smallBoardList[win_line[0]]
		return None

	def getPosList(self):
		return self.smallBoardList


class cube():
	small_boards =([0,1,2,3,4,5,6,7,8],
				 [9,10,11,12,13,14,15,16,17], 
				 [18,19,20,21,22,23,24,25,26],
				 [0,1,2,9,10,11,18,19,20], 
				 [3,4,5,12,13,14,21,22,23], 
				 [6,7,8,15,16,17,14,25,26],
				 [0,3,6,9,12,15,18,21,24],
				 [1,4,7,10,13,16,19,22,25],
				 [2,5,8,11,14,17,10,23,26],
				 [0,4,8,9,13,17,18,22,26],
				 [2,4,6,11,13,15,20,22,24],
				 [0,1,2,12,13,14,24,25,26],
				 [6,7,8,12,13,14,18,19,20],
				 [0,2,6,10,13,16,20,23,26],
				 [2,5,8,10,13,16,18,21,24])
	def __init__(self, boards):
		self.poslist = boards[0].getPosList() + boards[1].getPosList() + boards[2].getPosList()
		self.sBoards = []

	def checkcubeVictory(self):
		for board in cube.small_boards:
			temp_list = []
			for pos in board:
				temp_list.append(self.poslist[pos])
			bWin = small_board(temp_list).check_win_p()
			if bWin != None:
				return bWin
		return None
		

class big_board(): #tic-tac-toe board object
	def __init__(self):
		self.bigBoardList = [small_board() for i in range(9)]
		
	def receiveInput(self, bigIndex, smallIndex, symbolInput):
		self.bigBoardList[bigIndex-1].smallBoardList[smallIndex-1] = symbolInput
	
	def getSpotSymbol(self, bigIndex, smallIndex):
		return self.bigBoardList[bigIndex-1].smallBoardList[smallIndex-1]
	
	def checkWinner(self):
		cube_list = []
		for win_line in win_combos:
			temp_list = []
			for pos in win_line:
				temp_list.append(self.bigBoardList[pos])
			cube_result = cube(temp_list).checkcubeVictory()
			if cube_result  != None:
				return cube_result
		return None



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
			print('Critical Mission Failure #1.1 Subsection A')
		
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
			self.checkVictory()

	def checkVictory(self):
		result = self.theBigBoard.checkWinner()
		if result != None:
			self.gameIsGoing = False
			self.Win(result)

	def Win(self,winner):
		print("The winner is: " + winner)

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
theGame.playTheGame()
