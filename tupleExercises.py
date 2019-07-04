# Tuple Exercises 
# The data is unmutable, means cannot be changed 
# Tuples are fasters then list 


#List uses [] and tuple uses ()
#List and tuple both accept duplicate data 

months = ('January','February','March','April','May','June','July','August',
'September','October','November','December')

print(months)
print(type(months))


# Tuple can be used as the key in dictionary
# List cannot be used as the key in dictionary 
# In following example, officeLocation is an dictionary (key, value)
# this key (10.4456,56.8634) is a tuple 

officeLocation = {
    (10.4456,56.8634): "Helsinki",
    (29.4456,75.8634): "Oslo",
    (56.4456,11.8634): "Stolkholm"
}

print("Office location: ", officeLocation[(10.4456,56.8634)] )

# The individual items in dictionaty is actually a tuple  
print(officeLocation.items())

# Tuple Exercises 
# The data is unmutable, means cannot be changed 


#List uses [] and tuple uses ()
#List and tuple both accept duplicate data 

months = ('January','February','March','April','May','June','July','August',
'September','October','November','December')

print(months)
print(type(months))


# Tuple can be used as the key in dictionary
# List cannot be used as the key in dictionary 
# In following example, officeLocation is an dictionary (key, value)
# this key (10.4456,56.8634) is a tuple 

officeLocation = {
    (10.4456,56.8634): "Helsinki",
    (29.4456,75.8634): "Oslo",
    (56.4456,11.8634): "Stolkholm"
}

print("Office location: ", officeLocation[(10.4456,56.8634)] )

# The individual items in dictionaty is actually a tuple  
print(officeLocation.items())



# Looping - very simple and straightforward
# Using for loop 

for month in months:
    print(month)

# Using while loop , print months in reverse 

i = len(months) - 1 # the index is 11.. so  length 12 - 1 = 11 
while i >= 0:
    print("Month: ", months[i])
    i -= 1 


# Count operation: 

numbers = (1,1,2,2,2,3,3,3,3,3,3)
print("Number count 1: ", numbers.count(1)) # index 0 
print("Number count 2: ", numbers.count(2)) # index 2 # will show the first index only
print("Number count 3: ", numbers.count(3)) # index 5 
print("Index of 3: ", numbers.index(85)) # ValueError: tuple.index(x): x not in tuple 


# Nested tuple: 

numbers = (1,2,(3,4),(5,6,7),8,9)

print("Print tuple items", numbers[3]) # (5, 6, 7)   

# slices 

numbers = (1,2,(3,4),(5,6,7),8,9)

print("Print tuple slices ", numbers[0:3]) # (1,2,(3,4)) 

# steping 

print("Print tuple slices ", numbers[0:3:2]) # (1,(3,4)) 


