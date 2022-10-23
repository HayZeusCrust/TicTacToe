from location import Location,Value
import sys

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
		#First block gap
		print("   ",end="")
		#Column numbers
		for colNum in range(len(self.rows)):
			print("| "+str(colNum)+" ",end="")
		#Each consecutive row
		for rowNum,row in enumerate(self.rows):
			#Row seperator
			print("\n---------------")
			#Row header
			print(" "+str(rowNum)+" ",end="")
			#Each column in row
			for location in row:
				print("| "+str(location.value.value)+" ",end="")
