from random import randint

print("Let's play Rock, Paper, Scissor:")
print("Game Started... ")


player = input("Player, make your move: ").lower()

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
	else: 
		print("computer wins") # computer=="paper" is the only option 
	

elif player == "paper":
	if computer=="rock":
		print("Player wins")
	else:
		print("computer wins") # computer=="scissors" is the only option 

elif player == "scissors":
	if computer== "paper":
		print("Player wins")
	else: 
		print("computer  wins") # computer=="rock" is the only option 

else: 
	print("Please enter a valid move!")
