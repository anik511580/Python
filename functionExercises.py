# Function exercises - Part 1 


# Defining a simple function 

def sing_happy_birthday():
    print("Happy Birth Day to you")
    print("Happy Birth Day to you")
    print("Happy Birth Day dear sweetheart")
    print("Happy Birth Day to you")
    
sing_happy_birthday()
sing_happy_birthday()
sing_happy_birthday()

# Defining a function with return value

def square_of_7():
 return 7**2

result = square_of_7()
print(result) # 49


# return means exiting the code/program
# so does not execute whatever after the return

def square_of_7():
 return 7**2
 print("The program is exited when it gets return keyword ")

result = square_of_7()
print(result) # 49 



# Working on a random return function 

from random import random

def flip_coin():
    r = random() # By default, generates a random number between 0 to 1
    if r > 0.5:
        return "Heads"
    else:
        return "Tailss"
    
print(flip_coin())
    
# The previous program witbe better coding 

from random import random

def flip_coin():
    if random() > 0.5:
        return "HEAD"
    else:
        return "TAIL"
    
print(flip_coin()) # for a same function, it will override the previous one 
    

# Generating even numbers 

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]
    
print(generate_evens()) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]                           


# Function to generate square with a parameter that accepts a value  

def square(num):
    return num*num

print("The square is : ",  square(4)) # The square is : 16 

# Defining a birthday function with an argument 

def sing_happy_birthday(name):
    print("Happy Birth Day to you")
    print("Happy Birth Day to you")
    print(f"Happy Birth Day dear {name}")
    print("Happy Birth Day to you")
    
sing_happy_birthday("Ognila")
sing_happy_birthday("Anik")



# Multiple function 

def sum(a,b):
    return a+b

print("The sum is : ",  sum(2,3))



# Parameters vs argument 

def square (num):# this num is parameter 
    return num*num

print("The square is : ", square(7)) # this 7 is argument 


# lowercase to uppercase using function

def yell(word):
    return word.upper() + "!" 

yell("hello friends") # HELLO FRIENDS!


# Default parameters 
# will have a default value in the parameter
# if no argument is passed then default value is considered 

def sum(a = 1, b = 2):
    return a+b

print("The sum is : ",  sum()) # The sum is :  3                                                                                                        
print("The sum is : ",  sum(3,4)) # The sum is :  7                                                                                                        
print("The sum is : ",  sum(6)) # The sum is :  8  



# Keyword arguments 
# it allow us to define the argument know the exact name of the parameter 

def exponent(number, power):
    return number**power

print("The exponent is : ",  exponent(power = 2, number = 3)) # output: 9
print("The exponent is : ",  exponent(number = 3, power = 2)) # output: 9


# Variable scope 
# *** This program will show error, 
# *** cause inside the sum() it is searching for a local variable called total


total = 0  # global variable 

def sum():
    total += 1 
    return total 
    
sum()


# Variable scope 
# *** This last program can be solved this way...  
# *** write global before the variable name 


total = 0 

def sum():
    global total #global total help the program to take the value from global  
    total += 1 
    return total 
    
print(sum()) # output: 1 


# Documenting Function
# Use """ """ as the message 


total = 0 

def sum():
    """ Simple function to increament a number """

    global total    
    total += 1 
    return total 
    
print(sum()) # output: 1 
print(sum.__doc__)  # output: Simple function to increament a number
