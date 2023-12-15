from getkey import getkey,keys
import sys
import os

from board import Board,changeBoardSize
from menu import Title
from game import Game

#Generate .exe: pyinstaller.exe --console --onefile TicTacToe.py

"""
# To change the color of the Terminal Window
cmd = 'color 5E'     
os.system(cmd)
"""
# TODO : Use prompt_toolkit to make the graphics not ass (https://github.com/trevorbayless/cli-chess) : Reference
# TODO : Make options have scrollable settings
# TODO : Rework menus to be a method
# TODO : Finish game screen
# TODO : Change board size prompts
# TODO : Change enter name prompts
# TODO : Add setuptools package to automatically install stuff
# TODO : Game with create a config file if there isn't one to save settings
# TODO : Add match replay which save as a txt file
# TODO : Add player colors to settings
# TODO : Add option to forfeit game
# TODO : Add setting to pick which Title header you want
# TODO : turn into an exe that will open cmd on its own

def main():
	#Set window title
	os.system('title Tic-Tac-Toe')
	#Main menu options
	mainMenuOptions=["Player VS   AI  ","Player VS Player","Settings","Instructions","Exit"]
	selectedOption=0
	#Continue program until user exits
	while True:
		#Prepare the console
		os.system("mode 60,30")
		os.system('cls')
		#Welcome message
		print(
			"╔══════════════════════════════════════════════════════════╗\n"+
			"║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n"+
			"║░█████╗█╗░███╗░░░░█████╗░███╗░░███╗░░░░█████╗░███╗░█████╗░║\n"+
			"║░╚═█╔═╝█║█╔══█╗░░░╚═█╔═╝█╔══█╗█╔══█╗░░░╚═█╔═╝█╔══█╗█╔═══╝░║\n"+
			"║░░░█║░░█║█║░░╚╝███╗░█║░░█████║█║░░╚╝███╗░█║░░█║░░█║████╗░░║\n"+
			"║░░░█║░░█║█║░░█╗╚══╝░█║░░█╔══█║█║░░█╗╚══╝░█║░░█║░░█║█╔══╝░░║\n"+
			"║░░░█║░░█║╚███╔╝░░░░░█║░░█║░░█║╚███╔╝░░░░░█║░░╚███╔╝█████╗░║\n"+
			"║░░░╚╝░░╚╝░╚══╝░░░░░░╚╝░░═╝░░╚╝░╚══╝░░░░░░╚╝░░░╚══╝░╚════╝░║\n"+
			"║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n"+
			"╚══════════════════════════════════════════════════════════╝\n\n")
		#Menu select
		for numOption in range(len(mainMenuOptions)):
			print(" "*((60-len(mainMenuOptions[numOption]))//2-2),end="")
			if numOption==selectedOption:
				print("[ "+mainMenuOptions[numOption]+" ]\n")
			else:
				print("  "+mainMenuOptions[numOption]+"\n")
		pressedKey=getkey()
		#Resolve user input
		match pressedKey:
			#Move arrow up
			case "w"|keys.UP:
				selectedOption=(selectedOption-1)%len(mainMenuOptions)
			#Move arrow down
			case "s"|keys.DOWN:
				selectedOption=(selectedOption+1)%len(mainMenuOptions)
			#Handle selection
			case keys.SPACE|keys.ENTER:
				match selectedOption:
					#Play game with 1 human and 1 AI
					case 0:
						# TODO: code AI
						print("I'm implementing AI later lol")
					#Play game with 2 humans
					case 1:
						game=Game(2)
						game.play()
					#List game options
					case 2:
						optionsMenu()
					#Print instructions
					case 3:
						# TODO: Include instructions
						print("Instructions WIP")
					#Exit game
					case 4:
						sys.exit(0)
					#This should like never happen
					case _:
						print("Bro you broke the game lol")
			#Ignore all other keys
			case _:
				pass

def optionsMenu():
	#Options options
	optionsOptions=["Board Size : "+str(Board.numRows)+"x"+str(Board.numCols),"AI Difficulty : ","Back"]
	selectedOption=0
	while True:
		#Prepare the console
		os.system("mode 60,30")
		os.system('cls')
		#Welcome message
		print(
			"╔══════════════════════════════════════════════════════════╗\n"+
			"║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n"+
			"║░░░░░░░░░░░███╗░████╗░█████╗█╗░███╗░█╗░░█╗░████╗░░░░░░░░░░║\n"+
			"║░░░░░░░░░░█╔══█╗█╔══█╗╚═█╔═╝█║█╔══█╗██╗░█║█╔═══╝░░░░░░░░░░║\n"+
			"║░░░░░░░░░░█║░░█║████╔╝░░█║░░█║█║░░█║█╔█╗█║╚███╗░░░░░░░░░░░║\n"+
			"║░░░░░░░░░░█║░░█║█╔══╝░░░█║░░█║█║░░█║█║╚██║░╚══█╗░░░░░░░░░░║\n"+
			"║░░░░░░░░░░╚███╔╝█║░░░░░░█║░░█║╚███╔╝█║░╚█║████╔╝░░░░░░░░░░║\n"+
			"║░░░░░░░░░░░╚══╝░╚╝░░░░░░╚╝░░╚╝░╚══╝░╚╝░░╚╝╚═══╝░░░░░░░░░░░║\n"+
			"║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║\n"+
			"╚══════════════════════════════════════════════════════════╝\n\n")
	#Menu select
		for numOption in range(len(optionsOptions)):
			print(" "*((60-len(optionsOptions[numOption]))//2-2),end="")
			if numOption==selectedOption:
				print("[ "+optionsOptions[numOption]+" ]\n")
			else:
				print("  "+optionsOptions[numOption]+"\n")
		pressedKey=getkey()
		#Resolve user input
		match pressedKey:
			#Move arrow up
			case "w"|keys.UP:
				selectedOption=(selectedOption-1)%len(optionsOptions)
			#Move arrow down
			case "s"|keys.DOWN:
				selectedOption=(selectedOption+1)%len(optionsOptions)
			#Handle selection
			case keys.SPACE|keys.ENTER:
				match selectedOption:
					#Play game with 1 human and 1 AI
					case 0:
						changeBoardSize()
						optionsOptions[0]="Board Size: "+str(Board.numRows)+"x"+str(Board.numCols)
					#Play game with 2 humans
					case 1:
						# TODO: still code AI
						print("No AI yet ;-;")
					#List game options
					case 2:
						break
					case _:
						print("Bro you broke the game lol")
			#Ignore all other keys
			case _:
				pass

if __name__=="__main__":
	main()
