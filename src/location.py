from enum import Enum

#Possible values for a location
class Value(Enum):
	EMPTY=" "
	X="X"
	O="O"

#Object to describe a spots cords on a board and the mark on it
class Location:
	#Location constructor
	def __init__(self,row,col):
		self.row=row
		self.col=col
		self.value=Value.EMPTY
