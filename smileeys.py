

# Using for loop

print("Printing once using for loop: ")

for num in range(1,11):
	print("* " * num)


# Printing the same thing 3 times sing for  loop

print("Printing 3 times using nested loop: ")

for x in range(3):
	for num in range(1,11):
		print("* " * num)


# Using while loop 

print("Using while loop: ")

count = 1

while count < 11: 
	print("* " * count)
	count += 1 

# Using nested both do and while loop 

print("Without string multiplication:  ")


for num in range(1,11):
	count = 1
	stars = ""
	while count <= num:
		stars += "* "
		count += 1
	print(stars)

		
