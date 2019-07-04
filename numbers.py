
print(" \n Option 1: \n")


for num in range (1,21):
	
	if num == 4 or num == 13:
		print(f"{num} is UNLUCKY")
	elif num % 2==0: 
		print(f"{num} is even")
	else:
		print(f"{num} is odd")



#Option 2 for the same thing:
	
print("\n Option 2: \n")

for num in range (1,21):
	if num == 4 or num == 13:
		state = "UNLUCKY"
	elif num % 2==0: 
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")



