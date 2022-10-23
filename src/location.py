from enum import Enum

class Value(Enum):
	EMPTY=" "
	X="X"
	O="O"

class Location:
	def __init__(self,row,col):
		self.row=row
		self.col=col
		self.value=Value.EMPTY
