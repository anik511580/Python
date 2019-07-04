#Dictionary Exercises


#simple way to create dictionary
dictionary1 = {"name":"anik", "age":24}
print(dictionary1)

#create dictionary with dict()
dictionary2 = dict(name="anika", age=18)
print(dictionary2)

print(dictionary1["name"])
print(dictionary2["age"])

#accessing the dictionary values
for val in dictionary2.values():
    print(val)
    
#printing the dictionary keys
for val in dictionary2.keys():
    print(val)
    
#access the dictionary by f string
#for val, key in dictionary2.items():
    #print(f"key is {val} and value is {key}")
    

#access the values and make sum     
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
 
total_donations = 0
 
for donation in donations.values(): #access the values only
 total_donations += donation
 
print("total donation: ", total_donations)


#Cheak if a key is present
# "sam" in donation #True
# "sami" in donation.values() #False

# Dictionary methods

# copy
d = dict(a=1, b=2, c=3)
c= d.copy()
print("List c  is: ", c) # c==d but c is not d 

# clear
d = dict(a=1, b=2, c=3)
d.clear()
print("List d is: ", d)

# 
new_user = {}.fromkeys([])
print("New user: ", new_user)
new_user = {}.fromkeys(['name', 'address', 'phone'], 'Not Applicable') #normally used to default values
print("New user: ", new_user)
new_user = {}.fromkeys(['country'], 'Bangladesh') #sets key and value 
print("New user: ", new_user)
new_user = {}.fromkeys('school', 'Integrify') #for single quote every letter is counted 
print("New user: ", new_user)

#get 
a = dict(a=1, b=2, c=3)
print(a.get('a')) 
print(a.get('b')) 
print(a.get('c')) 
print(a.get('d')) # doesn't show error if get is ised 


# Program to check if a value is present in the dictionary 

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) 
 
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print("{} left".format(bakery_stock[food])) # format works like f string 
else:
    print("We don't make that")

#pop    

x = {"name":"anik", "age":24, "ages":34}
print(x)
y = x.pop('ages')
print(y)
print(x)


#update

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)


# Sample song dictionary 

playlist = {
    'title': 'lux express',
    'author': 'lux authority',
    'music' : [
        {'title': 'beat it', 'artists':'MJ', 'duration': 2.5},
        {'title': 'love me', 'artists':'CR7', 'duration': 3.45},
        {'title': 'destroy', 'artists':'DJ Snake', 'duration': 1.5}
    ]
}

print(playlist)


for song in playlist['music']:
    print(song['title'])


# Dictionary comprehension

numbers = dict(first = 1, second = 2, third = 3)
print("Normal numbers: ", numbers)
squaredNumbers= {key:value**2 for key, value in numbers.items() }
print("Squared numbers: ", squaredNumbers)


# Self created list comprehension 

selfCreatedList =  {num:num**3  for num in [1,2,3,4,5]}
print(selfCreatedList)


selfCreatedList2 =  {num:num**3  for num in range(1,11)}
print(selfCreatedList2)


# Assigning key and value by index 

string1 = "ABCDE"
string2 = "12345"

combileDic = { string1[i]:string2[i]  for i in range(0,len(string1))}
print(combileDic)

# accessing the dictionary 

infoDictionary = {"name":"anik", "school":"integrify", "city": "helsinki"}

infoDictionary_upper = {k.upper():v.upper()  for k,v in infoDictionary.items()}

print(infoDictionary_upper)


# playing with the dictionary 

numList = [1,2,3,4,5,6]

evenOddList = {num:("even" if num % 2 == 0 else "odd")  for num in numList}

print(evenOddList)


evenOddList2 = {num:("even" if num % 2 == 0 else "odd")  for num in range(1,100)}

print(evenOddList2)


#Assigning values from 2 lists 


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}
print(answer)


# Accessing the items 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer1 = {thing[0]: thing[1] for thing in person} # name = Jared etc 
answer2 = dict(person)

print(answer1)
print(answer2)


# Assigning o to the vowels 
answer = {char:0 for char in 'aeiou'}
print(answer)

answer2 = dict.fromkeys("aeiou", 0) 
print(answer2)


#ASCI code count 
answer = {count: chr(count) for count in range(65,91)}
print(answer)
