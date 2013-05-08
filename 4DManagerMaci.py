import bigBoard
import smallBoard
import random
from random import choice

#the possible small board win combinations: 
win_combos =([0, 1, 2],
			 [3, 4, 5], 
			 [6, 7, 8],
			 [0, 3, 6], 
			 [1, 4, 7], 
			 [2, 5, 8],
			 [0, 4, 8],
			 [2, 4, 6])

#A small 3x3 board
class small_board():

	#initialzied the list of empty spots
	def __init__(self,posList=0):
		if posList == 0:
			self.smallBoardList = [" " for i in range(9)]
		else:
			self.smallBoardList = posList

	#checks to see if there is a small board win
	def check_win_p(self):
		for win_line in win_combos:
			if self.smallBoardList[win_line[0]] != " " and self.smallBoardList[win_line[0]] == self.smallBoardList[win_line[1]] and self.smallBoardList[win_line[1]] == self.smallBoardList[win_line[2]]:
				return self.smallBoardList[win_line[0]]
		return None

	#returns the board list
	def check_possible_win(self):
		possible_win_dict = {}
		for win_line in win_combos:
			if self.smallBoardList[win_line[0]] != " " or self.smallBoardList[win_line[1]] != " " or self.smallBoardList[win_line[2]] != " ":
				if self.smallBoardList[win_line[0]] == self.smallBoardList[win_line[1]] and self.smallBoardList[win_line[2]] == " ":
					if self.smallBoardList[win_line[0]] in possible_win_dict:
						possible_win_dict[self.smallBoardList[win_line[0]]].append(win_line[2])
					else:
						possible_win_dict[self.smallBoardList[win_line[0]]] = [win_line[2]]
				if self.smallBoardList[win_line[1]] == self.smallBoardList[win_line[2]] and self.smallBoardList[win_line[0]] == " ":
					if self.smallBoardList[win_line[1]] in possible_win_dict:
						possible_win_dict[self.smallBoardList[win_line[1]]].append(win_line[0])
					else:
						possible_win_dict[self.smallBoardList[win_line[1]]] = [win_line[0]]
				if self.smallBoardList[win_line[0]] == self.smallBoardList[win_line[2]] and self.smallBoardList[win_line[1]] == " ":
					if self.smallBoardList[win_line[0]] in possible_win_dict:
						possible_win_dict[self.smallBoardList[win_line[0]]].append(win_line[1])
					else:
						possible_win_dict[self.smallBoardList[win_line[0]]] = [win_line[1]]
		return possible_win_dict

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
				 [0,3,6,10,13,16,20,23,26],
				 [2,5,8,10,13,16,18,21,24])
	def __init__(self, boards, board_pos = [-1,-1,-1]):
		self.poslist = boards[0].getPosList() + boards[1].getPosList() + boards[2].getPosList()
		self.sBoards = []
		self.board_num = board_pos

	def checkcubeVictory(self):
		for board in cube.small_boards:
			temp_list = []
			for pos in board:
				temp_list.append(self.poslist[pos])
			bWin = small_board(temp_list).check_win_p()
			if bWin != None:
				return bWin
		return None
		
#big board containing 9 small boards
class big_board():
	#initializes the list of small boards
	def check_possible_win_cube(self):
		possible_wins_dict = {}
		for board in cube.small_boards:
			temp_list = []
			for pos in board:
				temp_list.append(self.poslist[pos])
			p_wins = small_board(temp_list).check_possible_win()
			temp_wins = {}
			for key, value in p_wins.items():
				temp_win_pos_list = []
				for pos in value:
					temp_win_pos_list.append((self.board_num[board[pos]//9],int(board[pos]%9)))
				temp_wins[key] = temp_win_pos_list
			possible_wins_dict = self.merge_2_dict_list(possible_wins_dict, temp_wins)
		return possible_wins_dict

	def merge_2_dict_list(self, dict1, dict2):
		keys = list(dict1.keys()) + list(dict2.keys())
		new_dict = {}
		for key in keys:
			if key in dict1 and key in dict2:
				new_dict[key] = dict1[key]  + dict2[key]
				new_list = []
				for elem in new_dict[key]:
					if elem not in new_list:
						new_list.append(elem)
				new_dict[key] = new_list
			elif key in dict1:
				new_dict[key] = dict1[key]
			elif key in dict2:
				new_dict[key] = dict2[key]
		return new_dict

class big_board(): #tic-tac-toe board object
	def __init__(self):
		self.bigBoardList = [small_board() for i in range(9)]
		
	#acceps inputs into list
	def receiveInput(self, bigIndex, smallIndex, symbolInput):
		self.bigBoardList[bigIndex-1].smallBoardList[smallIndex-1] = symbolInput
	
	#returns the symbol at the postions
	def getSpotSymbol(self, bigIndex, smallIndex):
		return self.bigBoardList[bigIndex-1].smallBoardList[smallIndex-1]
	
	#uses cube class to check for victory on big board
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

	def check_possible_win(self):
		possible_wins_dict = {}
		cube_list = []
		for win_line in win_combos:
			temp_list = []
			for pos in win_line:
				temp_list.append(self.bigBoardList[pos]) 
			p_wins = cube(temp_list,win_line).check_possible_win_cube()
			possible_wins_dict = self.merge_2_dict_list(possible_wins_dict, p_wins)
		return possible_wins_dict

	def merge_2_dict_list(self, dict1, dict2):
		keys = list(dict1.keys()) + list(dict2.keys())
		new_dict = {}
		for key in keys:
			if key in dict1 and key in dict2:
				new_dict[key] = dict1[key]  + dict2[key]
				new_list = []
				for elem in new_dict[key]:
					if elem not in new_list:
						new_list.append(elem)
				new_dict[key] = new_list
			elif key in dict1:
				new_dict[key] = dict1[key]
			elif key in dict2:
				new_dict[key] = dict2[key]
		return new_dict

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
		
#the class to actually run a game and manage players
class aGame():
	#initializes a single big board
	def __init__(self):
		self.theBigBoard = big_board()
	
	#asks players to input the symbols that will be used for the various players
	def getPlayersSymbol(self):
		isValidInput = False
		self.playersSymbol = []
		for i in range(0, self.numPlayers):
			isValidInput = False
			while(not isValidInput):
				try:
					inputAsk = input("Player number " + str(i+1) + " symbol is: ")
					if(len(inputAsk) == 1 and inputAsk != " "):
						if(not(inputAsk in self.playersSymbol)):
							self.playersSymbol += [inputAsk]
							isValidInput = True
						else:
							print("That character has already been taken")
					else:
						print("Please input a single character")
						raise ValueError
				except ValueError:
					isValidInput = False
		self.printPlayers()
	
	#prints out a list of who the players are and their corresponding symbols
	def printPlayers(self):
		for i in range(0, self.numPlayers):
			print("Player " + str(i + 1) + " is symbol " + self.playersSymbol[i])

	#asks a human player to input a move, then checks that it is valid
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
		#displays the players at the end
		self.theBigBoard.receiveInput(bigIndexMove,smallIndexMove, self.playersSymbol[self.currentTurn])
			
	#starts a game by getting player types and symbols
	def startGame(self):
		self.currentTurn = 0
		self.getPlayerTypes()
		self.getPlayersSymbol()
		
	#prints the whole board
	def showBoard(self):
		self.theBigBoard.print_board()
	
	#looks at type of player and makes turn accordingly
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
	
	#the AI movement behavior
	def makeAIMove(self):
		best_move = ()
		p_wins = self.theBigBoard.check_possible_win()
		print(p_wins)
		total_blocks = 0
		moves_away = -1
		player_order_list = self.playersSymbol[self.currentTurn:] + self.playersSymbol[:self.currentTurn]
		print(player_order_list)
		for player in player_order_list:
			if player in p_wins:
				if total_blocks>=moves_away:
					best_move = choice(p_wins[player])
					break
				total_blocks += len(p_wins[player])
			moves_away += 1
		print(best_move)
		if len(best_move) == 0:
			self.askForInput()
		else:
			self.theBigBoard.receiveInput(best_move[0]+1,best_move[1]+1, self.playersSymbol[self.currentTurn])

	#Makes random monkey move
	def makeMonkeyMove(self):
		#try one until it finds an empty one
		isValidMove = False
		while(not isValidMove):
			bigIndex = random.randint(0,8)
			smallIndex = random.randint(0,8)
			
			if(self.theBigBoard.getSpotSymbol(bigIndex, smallIndex) == " "):
				isValidMove = True
				
		self.theBigBoard.receiveInput(bigIndex,smallIndex, self.playersSymbol[self.currentTurn])
		
	#plays a full game until game is done
	def playTheGame(self):
		self.gameIsGoing = True
		while(self.gameIsGoing):
			self.nextTurn()
			self.currentTurn += 1
			if(self.currentTurn == self.numPlayers):
				self.currentTurn = 0
			self.checkVictory()

	#checks for a winner 
	def checkVictory(self):
		result = self.theBigBoard.checkWinner()
		if result != None:
			self.gameIsGoing = False
			self.Win(result)

	#shows board and who the winner is
	def Win(self,winner):
		self.showBoard()
		print("The winner is: " + winner)

	#gets the player types (monkey, ai, human)
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
