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
			while not moveValid:
				moveValid,error=self.isValidMove(input(str(currentPlayer.name)+" select a square to mark: row column\n"))
				print(error)
			
			#Swap active players
			if currentPlayer==self.playerX:
				return self.playerO
			else:
				return self.playerX
				
	#Validate move selection
	def isValidMove(self,move):
		if " " not in move:
			return False,"Move coordinates are not seperated by a space"
		move=move.split(" ")
		if len(move>2):
			return False,""
		return True,""