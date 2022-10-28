from board import Board,changeBoardSize
from game import Game
import sys

#Generate .exe: pyinstaller.exe --console --onefile TicTacToe.py

"""
import os

# To check the size of the Terminal Window
x = os.get_terminal_size().lines
y = os.get_terminal_size().columns
print(x)
print(y)

# To change the size of the Terminal Window
cmd = 'mode 50,20'
os.system(cmd)

# To change the color of the Terminal Window
cmd = 'color 5E'     
os.system(cmd)
"""
# TODO : import msvcrt for pretty menu
# TODO : Make screen clear before prints and set size to 60x30
# TODO : automatically change window to be correct size
# TODO : turn into an exe that will open cmd on its own
# TODO : Game with create a config file if there isn't one to save settings
# TODO : Add match replay which save as a txt file
# TODO : Add player colors to settings
# TODO : Add option to forfit game
# TODO : Add setting to pick which Title header you want

def main():
	#Welcome message
	print("\n"+
		"╔══════════════════════════════════════════════════════════╗\n"+
		"║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n"+
		"║░█████╗█╗░███╗░░░░█████╗░███╗░░███╗░░░░█████╗░███╗░█████╗░║\n"+
		"║░╚═█╔═╝█║█╔══█╗░░░╚═█╔═╝█╔══█╗█╔══█╗░░░╚═█╔═╝█╔══█╗█╔═══╝░║\n"+
		"║░░░█║░░█║█║░░╚╝███╗░█║░░█████║█║░░╚╝███╗░█║░░█║░░█║████╗░░║\n"+
		"║░░░█║░░█║█║░░█╗╚══╝░█║░░█╔══█║█║░░█╗╚══╝░█║░░█║░░█║█╔══╝░░║\n"+
		"║░░░█║░░█║╚███╔╝░░░░░█║░░█║░░█║╚███╔╝░░░░░█║░░╚███╔╝█████╗░║\n"+
		"║░░░╚╝░░╚╝░╚══╝░░░░░░╚╝░░═╝░░╚╝░╚══╝░░░░░░╚╝░░░╚══╝░╚════╝░║\n"+
		"║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n"+
		"╚══════════════════════════════════════════════════════════╝")	
	#Continue program until user leaves
	while True:
		#Menu select
		menuSelect=(-1)
		while not(1<=int(menuSelect)<=6):
			menuSelect=input("\nMain Menu:\n"+
				" 1. 1 Player\n"+
				" 2. 2 Players\n"+
				" 3. Options\n"+
				" 4. Instructions\n"+
				" 5. Credits\n"+
				" 6. Exit\n\n")
			#Resolve user input
			match menuSelect:
				#Play game with 1 human and 1 AI
				case "1":
					# TODO: code AI
					print("I'm implementing AI later lol")
				#Play game with 2 humans
				case "2":
					game=Game(2)
					game.play()
				#List game options
				case "3":
					optionsMenu()
				#Print instructions
				case "4":
					# TODO: Include instructions
					print("Instructions WIP")
				#Print credits
				case "5":
					# TODO: Make credits
					print("Credits WIP")
				#Exit game
				case "6":
					sys.exit(0)
				#Didn't input a numerical answer
				case _:
					print("Didn't select a numerical option")
					menuSelect=(-1)

def optionsMenu():
	optionSelect=(-1)
	while not(1<=int(optionSelect)<=3):
		optionSelect=input("\nOptions:\n"+
			"1. Board Size: "+str(Board.numRows)+"x"+str(Board.numCols)+"\n"+
			"2. AI Difficulty\n"+
			"3. Return to Menu\n\n")
		#Resolve option
		match optionSelect:
			#Change board size
			case "1":
				changeBoardSize()
				optionSelect=(-1)
			#Change difficulty of AI
			case "2":
				# TODO: still code AI
				print("No AI yet ;-;")
			#Return to menu
			case "3":
				pass
			#Didn't input a numerical answer
			case _:
				print("Didn't select a numerical option")
				optionSelect=(-1)

if __name__=="__main__":
	main()
