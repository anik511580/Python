#Example 1: Type exit to break

print("Example 1: ")

while True:
	command = input("type 'exit' to exit \n")
	if (command == "exit"):
		break


#Example 2: exit from the program with a certain value

print("Example 2: ")


for x in range(1,101):
	print(x)
	if x==30:
		break
