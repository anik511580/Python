import random 

random_number = int (random.randint(1,10) )  # numbers 1 to 10

guess = input("Guess a number between 1 to 10: ")
guess = int(guess)

if guess == random_number:
	print("You got it")
elif guess < random_number:
	print("too low")
else:
	print("too high")

#random_number = str(random_number)
print("The actual number is : " + str(random_number))  