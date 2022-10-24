from game import Game
import sys

def main():
	#Continue game until user leaves
	while True:
		#Welcome message
		print("Welcome to Tic-Tac-Toe!!!\n")
		#Menu select
		menuSelect=""
		while not(menuSelect=="1" or menuSelect=="2" or menuSelect=="3" or menuSelect=="4"):
			menuSelect=input("Please select an option:\n\n1. 1 Player\n2. 2 Players\n3. Credits\n4. Exit\n\n")
		#Resolve user input
		match menuSelect:
			#Play game with 1 human and 1 AI
			case "1":
				print("I'm implementing AI later lol")
			#Play game with 2 humans
			case "2":
				game=Game()
				game.play()
			#Print credits
			case "3":
				print("Credits WIP")
			#Exit game
			case "4":
				sys.exit(0)
			#You broke the game lol
			case _:
				print("How did we get here?")
				sys.exit(-1)

if __name__=="__main__":
	main()
