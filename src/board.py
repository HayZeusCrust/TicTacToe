from location import Location

#Object to represent the game board
class Board:
	#Board constructor
	def __init__(self):
		rows=[]
		for row in range(3):
			currentRow=[]
			for col in range(3):
				currentRow.append(Location(row,col))
			rows.append(currentRow)
		self.rows=rows
	
	#Prints the game board
	def printBoard(self):
		#Print board row by row
		for rowNum,row in enumerate(self.rows):
			#Row seperator
			print("-------------")
			#Print each column in a row
			for location in row:
				print("| "+str(location.value.value)+" ",end="")
			#Cap cloumns
			print("|")
		#Cap rows
		print("-------------")
