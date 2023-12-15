from location import Location

#Object to represent the game board
class Board:
	#Class variables
	numRows=3
	numCols=3
	winSize=3
	
	#Board constructor
	def __init__(self):
		rows=[]
		for row in range(Board.numRows):
			currentRow=[]
			for col in range(Board.numCols):
				currentRow.append(Location(row,col))
			rows.append(currentRow)
		self.rows=rows
		self.remainingSpaces=Board.numRows*Board.numCols
	
	#Prints the game board
	def printBoard(self,selectedRow,selectedCol):
		#Board start
		print("-"*(4*Board.numCols+1))
		#Print board row by row
		for row in self.rows:
			#Print each column in a row
			for location in row:
				if location.row==selectedRow and location.col==selectedCol:
					print("|["+str(location.value.value)+"]",end="")
				else:
					print("| "+str(location.value.value)+" ",end="")
			#Cap rows
			print("|\n"+"-"*(4*Board.numCols+1))

	def removeSpace(self):
		self.remainingSpaces-=1

def changeBoardSize():
	newRowSize=(-1)
	newColSize=(-1)
	while not(3<=newRowSize<=9):
		newRowSize=input("New number of board rows: (Min: 3, Max: 9)\n")
		try:
			newRowSize=int(newRowSize)
		except ValueError:
			newRowSize=(-1)
	while not(3<=newColSize<=9):
		newColSize=input("New number of board columns: (Min: 3, Max: 9)\n")
		try:
			newColSize=int(newColSize)
		except ValueError:
			newColSize=(-1)
	Board.numRows=newRowSize
	Board.numCols=newColSize
	if newRowSize==3 or newColSize==3:
		Board.winSize=3
	else:
		Board.winSize=4
