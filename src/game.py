from location import Value
from player import Player
from board import Board

class Game:
	def __init__(self,numPlayers):
		#Create a board for the game
		self.board=Board()
		#Create player X with default name Player 1
		playerName=input("Player 1 name: ")
		if playerName=="":
			playerName="Player X"
		self.playerX=Player(playerName,Value.X)
		#Create player O with default name Player 2 if set to 2 players
		if numPlayers==2:
			playerName=input("Player 2 name: ")
			if playerName=="":
				playerName="Player O"
			self.playerO=Player(playerName,Value.O)
		#Set player O to AI if only 1 player
		else:
			pass
			#playerO=AI

	#Play a game with the selected players
	def play(self):
		currentPlayer=self.playerX
		#Keep taking turns until the game is over
		while True:
			#show current board
			self.board.printBoard()
			#Take player move
			moveValid=False
			move=""
			while not moveValid:
				moveValid,error,move=isValidMove(input(str(currentPlayer.name)+" select a square to mark: row column\n"),self.board)
				print(error)
			self.board.rows[move[0]][move[1]].value=currentPlayer.mark
			if checkWin(move[0],move[1],self.board,currentPlayer.mark):
				# TODO : Victory screen
				self.board.printBoard()
				break
			#Swap active players
			if currentPlayer==self.playerX:
				currentPlayer=self.playerO
			else:
				currentPlayer=self.playerX
				
#Validate move selection
def isValidMove(move,board):
	#Check cords are separated by a space
	if " " not in move:
		return False,"Row and column are not separated by a space",move
	move=move.split(" ")
	#Check only 2 cords are provided
	if len(move)!=2:
		return False,"Provide a row and a column",move
	#Check only ints are provided
	try:
		move[0]=int(move[0])-1
		move[1]=int(move[1])-1
	except ValueError:
		return False,"Row and column must be integers",move
	#Check move is in board range
	if not(0<=move[0]<Board.numRows and 0<=move[1]<Board.numCols):
		return False,"Row and column are out of board range",move
	#Check move space is empty
	if board.rows[move[0]][move[1]].value!=Value.EMPTY:
		return False,"Row and column are not empty",move
	return True,"Valid move",move

# TODO : Check win
"""Win conditions:
get 4 corners
make a square
get shorter of two dimensions in a row
"""
def checkWin(moveRow,moveCol,board,playerMark):
	#Check in a row win
	if checkRowWin(moveRow,moveCol,board,playerMark):
		return True
	if board.numRows==board.numCols!=3:
		pass
		#Check 4 corner win
		#Check square win
		# TODO : ^^^
	return False
	# TODO : Check board full if no winner
	
def checkRowWin(moveRow,moveCol,board,playerMark):
	for horizontalDirection in range(-1,1):
		for verticalDirection in range(-1,2):
			count=1
			if verticalDirection==horizontalDirection==0:
				break
			for swap in range(-1,2,2):
				checkRow=moveRow
				checkCol=moveCol
				try:
					while board.rows[NIE(checkRow+horizontalDirection*swap)][NIE(checkCol+verticalDirection*swap)].value==playerMark:
						checkRow+=horizontalDirection*swap
						checkCol+=verticalDirection*swap
						count+=1
				except IndexError:
					pass
			if count>=board.winSize:
				return True
	return False
	
#Negative Index Error
def NIE(index):
	if index<0:
		raise IndexError
	return index
