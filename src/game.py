from getkey import getkey,keys
import os

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
		#TODO : Set player O to AI if only 1 player
		else:
			pass
			#playerO=AI

	#Play a game with the selected players
	def play(self):
		#Initialize game variables
		currentPlayer=self.playerX
		selectedRow=0
		selectedCol=0
		#Keep taking turns until the game is over
		while True:
			#Prepare the console
			os.system("mode 60,30")
			os.system('cls')
			#Select your move
			while True:
				#Prepare the console
				os.system("mode 60,30")
				os.system('cls')
				#Show current board
				self.board.printBoard(selectedRow,selectedCol)
				print(" "+str(currentPlayer.name)+" select an empty square to mark")
				#Select a move
				pressedKey=getkey()
				match pressedKey:
					#Move selection up
					case "w"|keys.UP:
						selectedRow=(selectedRow-1)%self.board.numRows
					#Move selection down
					case "s"|keys.DOWN:
						selectedRow=(selectedRow+1)%self.board.numRows
					#Move selection left
					case "a"|keys.LEFT:
						selectedCol=(selectedCol-1)%self.board.numCols
					#Move selection right
					case "d"|keys.RIGHT:
						selectedCol=(selectedCol+1)%self.board.numCols
					#Make selected move if available
					case keys.SPACE|keys.ENTER:
						if self.board.rows[selectedRow][selectedCol].value==Value.EMPTY:
							break
					#Ignore all other keys
					case _:
						pass
			#Apply move to board
			self.board.rows[selectedRow][selectedCol].value=currentPlayer.mark
			self.board.removeSpace()
			#Check if current player won
			if checkWin(selectedRow,selectedCol,self.board,currentPlayer.mark):
				# TODO : Victory screen
				#Prepare the console
				os.system("mode 60,30")
				os.system('cls')
				#Print win screen
				self.board.printBoard((-1),(-1))
				print("Press enter to return to main menu")
				while getkey()!=keys.ENTER:
					pass
				break
			#Check for tie
			if self.board.remainingSpaces==0:
				# TODO : Tie screen
				#Prepare the console
				os.system("mode 60,30")
				os.system('cls')
				#Print tie screen
				self.board.printBoard((-1),(-1))
				print("Press enter to return to main menu")
				while getkey()!=keys.ENTER:
					pass
				break
			#Swap active players
			if currentPlayer==self.playerX:
				currentPlayer=self.playerO
			else:
				currentPlayer=self.playerX

def checkWin(moveRow,moveCol,board,playerMark):
	#Check in a row win
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
	#Non 3x3 wins
	if board.numRows==board.numCols!=3:
		#Check 4 corner win
		if board.rows[0][0].value==playerMark and \
		board.rows[0][board.numCols-1].value==playerMark and \
		board.rows[board.numRows-1][0].value==playerMark and \
		board.rows[board.numRows-1][board.numCols-1].value==playerMark:
			return True
		#Check square win
		for horizontalDirection in range(-1,2,2):
			for verticalDirection in range(-1,2,2):
				try:
					if board.rows[NIE(moveRow+horizontalDirection)][NIE(moveCol+verticalDirection)].value==playerMark:
						if board.rows[NIE(moveRow+horizontalDirection)][moveCol].value==board.rows[moveRow][NIE(moveCol+verticalDirection)].value==playerMark:
							return True
				except IndexError:
					pass
	return False

#Negative Index Error
def NIE(index):
	if index<0:
		raise IndexError
	return index
