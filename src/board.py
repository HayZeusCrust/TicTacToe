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
			print("-"*(4*len(row)+1))
			#Print each column in a row
			for location in row:
				print("| "+str(location.value.value)+" ",end="")
			#Cap cloumns
			print("|")
		#Cap rows
		print("-"*(4*len(row)+1))

	def changeBoardSize():
		newRowSize=(-1)
		newColSize=(-1)
		while not(int(newRowSize)>=3 and int(newRowSize)<=10):
			newRowSize=input("New number of board rows: (Min: 3, Max: 10)\n")
			try:
				newRowSize=int(newRowSize)
			except:
				newRowSize=(-1)
		while not(newColSize>=3 and newColSize<=10):
			newColSize=input("New number of board columns: (Min: 3, Max: 10)\n")
			try:
				newColSize=int(newColSize)
			except:
				newColSize=(-1)
		Board.numRows=newRowSize
		Board.numCols=newColSize