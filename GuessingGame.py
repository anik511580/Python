import random 

random_number = int (random.randint(1,10) )  # numbers 1 to 10

while True:
	guess = input("Guess a number between 1 to 10: ")
	guess = int(guess)
	if guess > random_number:
		print("too high")
	elif guess < random_number:
		print("too low")
	else:
		print("You got it")
		play_again = input("Do you wanna play again? (y/n)")
		if play_again == "y":
			random_number = int (random.randint(1,10) ) 
			guess = None
		
		else:
			print("Thanks for playing")
			break  
 