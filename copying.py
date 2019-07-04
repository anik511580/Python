# A simple copy program
# Ask from the input
# repeat the same thing what user said 
# program stop if input is "stop copying me"

msg = input ("Say something... \n")

while msg != "stop copying me":
	msg = input(f"{msg}\n" )
print("ok ok, you win. ")