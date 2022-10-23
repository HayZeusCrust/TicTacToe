from location import Location

class Board:
	def __init__(self):
		rows=[]
		for row in range(3):
			currentRow=[]
			for col in range(3):
				currentRow.append(Location(row,col))
			rows.append(currentRow)
		self.rows=rows

	def printBoard(self):
		#Each consecutive row
		for rowNum,row in enumerate(self.rows):
			#Row seperator
			print("-------------")
			#Each column in row
			for location in row:
				print("| "+str(location.value.value)+" ",end="")
			print("|")
		print("-------------")
