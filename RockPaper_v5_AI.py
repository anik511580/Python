from random import randint

player_wins=0
computer_wins=0
winning_score=3


while player_wins < winning_score and computer_wins < winning_score:
	

	print("Let's play Rock, Paper, Scissor")
	print("Just type: rock / paper / scissor:")
	print(f"Player Score: {player_wins} Computer Score: {computer_wins} ")
	print("Game Started... ")


	player = input("Player, make your move: ").lower()
	if player == "quit" or player == "q":
		break

	rand_num = randint(0,2)

	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
	 computer = "scissors"

	print(f"Computer plays: {computer}")
	  
	if player==computer:
		print("Match Draw!!!")

	elif player == "rock":
		if computer== "scissors":
			print("Player wins")
			player_wins+=1
		else: 
			print("computer wins") # computer=="paper" is the only option 
			computer_wins+=1

	elif player == "paper":
		if computer=="rock":
			print("Player wins")
			player_wins+=1

		else:
			print("computer wins") # computer=="scissors" is the only option 
			computer_wins+=1

	elif player == "scissors":
		if computer== "paper":
			print("Player wins")
			player_wins+=1
		else: 
			print("computer  wins") # computer=="rock" is the only option 
			computer_wins+=1
	else: 
		print("Please enter a valid move!")

if player_wins>computer_wins:
	print("CONGRATS, you won the game!")
elif player_wins==computer_wins:
	print("It's a tie... ")

else:
	print("Oh no... computer won :( ") 

print(f"Final Score: Player: {player_wins}, Computer: {computer_wins} ")

