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
	
	# TODO : Fix printing for 10x10 boards
	#Prints the game board
	def printBoard(self):
		#Column headers
		print("    ",end="")
		for col in range(Board.numCols):
			print(" "+str(col+1)+"  ",end="")
		#Row seperator
		print("\n   "+"-"*(4*Board.numCols+1))
		#Print board row by row
		for rowNum,row in enumerate(self.rows):
			#Row headers
			print(" "+str(rowNum+1)+" |",end="")
			#Print each column in a row
			for location in row:
				print(" "+str(location.value.value)+" |",end="")
			#Cap rows
			print("\n   "+"-"*(4*Board.numCols+1))

def changeBoardSize():
	newRowSize=(-1)
	newColSize=(-1)
	while not(3<=newRowSize<=10):
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
