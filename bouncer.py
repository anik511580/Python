# ask for age
# 18-20 years old, can enter but no drink
# 21+ entry and drink allowed 
# no input of age, show the message 

age = input("How old are you? ")


if age:
	age = int(age)


	if age >= 18 and age < 21:
		print("you can enter, but need a wristband. ")


	# 21+ drink + entry allowed 

	elif age >= 21:
		print(" you can enter and have a drink ")

	else:
		print("you are too little age, go to hell")

else:
	print("you must enter age")





