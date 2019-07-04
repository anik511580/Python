# Sets Exercises... 
# Sets do not have duplicate values 
# Sets are not ordered 
# Cannot be accessed by index 

# Printing set
numberSet = {1,2,3,4,4,4,5,5,5,5,5,5, 'a', 'b', 3.1416}
print("numberSet ", numberSet) # {1, 2, 3.1416, 4, 5, 3, 'a', 'b'} + random orders 


# Printing set 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Printing a duplicate list 

cities = ["Dhaka","Helsinki","Dhaka","Oslo","Helsinki"]

# Converting in Set
print(set(cities)) # {'Dhaka', 'Oslo', 'Helsinki'}
print(len(set(cities))) # Length is 3 


#Converting in List again
print(list(set(cities))) # ['Dhaka', 'Oslo', 'Helsinki']

#Add operation 

cities.add("Turku")

print(cities) # {'Oslo', 'Helsinki', 'Dhaka', 'Turku'}


# Remove operation

cities = {"Dhaka","Helsinki","Dhaka","Oslo","Helsinki","Turku","Turku"}

cities.remove("Turku")
print(cities)

cities.remove("Norway") # Gives error as "Norway" is not present

# Same task can be done by discard but it doesnt give error 
ities.discard("Norway")
 
# Copy 

cities = {"Dhaka","Helsinki","Dhaka","Oslo","Helsinki","Turku","Turku"}

cities2 = cities.copy()

print(cities)
print(cities2)

if (cities == cities2):
    print("cities == cities2")
if cities is cities2:
    print("cities is cities2")
else: 
    print("cities is NOT cities2") # Cause it creates duplicate memory


# clear operation

print(cities.clear()) # Output: None

# Set oparation
# Union operation 


ML_students = {"Anik","Peter","Sileshi","CR7","Messi","Klose"}
Web_students = {"Sileshi","CR7","Messi","Hola","Satana","Perkele"}

allStudents = ML_students | Web_students
print(allStudents)

# Common items in both sets 

bothStudents = ML_students & Web_students
print(bothStudents)


# Set comprehension 

# Using set:  
print({x**2 for x in range(10)}) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# Using dictionary (key:value):
print({x:x**2 for x in range(10)})  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}     

# Printing in upper case 
upper = {char.upper() for char in 'helsinki'}
print(upper)             






# Couple of more programs from the quiz 

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
 
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)
 
# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
 
# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
 
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff) # set values are unique always 