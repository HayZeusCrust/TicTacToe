from location import Location

#Object to represent the game board
class Board:
	#Class variables
	numRows=3
	numCols=3
	
	#Board constructor
	def __init__(self):
		rows=[]
		for row in range(Board.numRows):
			currentRow=[]
			for col in range(Board.numCols):
				currentRow.append(Location(row,col))
			rows.append(currentRow)
		self.rows=rows
	
	#Prints the game board
	def printBoard(self):
		#Print board row by row
		for rowNum,row in enumerate(self.rows):
			#Row seperator
			print("-"*(4*Board.numCols+1))
			#Print each column in a row
			for location in row:
				print("| "+str(location.value.value)+" ",end="")
			#Cap columns
			print("|")
		#Cap rows
		print("-"*(4*Board.numCols+1))

def changeBoardSize():
	newRowSize=(-1)
	newColSize=(-1)
	while not(3<=int(newRowSize)<=10):
		newRowSize=input("New number of board rows: (Min: 3, Max: 10)\n")
		try:
			newRowSize=int(newRowSize)
		except ValueError:
			newRowSize=(-1)
	while not(3<=newColSize<=10):
		newColSize=input("New number of board columns: (Min: 3, Max: 10)\n")
		try:
			newColSize=int(newColSize)
		except ValueError:
			newColSize=(-1)
	Board.numRows=newRowSize
	Board.numCols=newColSize
