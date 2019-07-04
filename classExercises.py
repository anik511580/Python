# Exercises on class 

# Defining a simple class

class User: 
    
    def __init__(self,first,last,age):
        self.first = first
        self.last = last 
        self.age = age 
user1 = User("Anik","Barua",25)
user2 = User("LingLing","Xue",23)

print(user1.first, user1.last)
print(user2.first, user2.last)


# Define the Comment class below

class Comment: 
    def __init__(self,username, text,likes=0):
        self.username = username
        self.text = text 
        self.likes = likes
    
another_comment = Comment("rosa77","soooo cute!!!")
print(another_comment.username, another_comment.text,another_comment.likes)


# User information using class.... 

class User: 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last 
        self.age = age 
        
    def full_name(self):
        return "First name: {}, Last name: {}".format(self.first, self.last)
        
    def initials(self):
        return "The initial format is: {}.{}.".format(self.first[0],self.last[0])
        
    def likes(self,food):
        return "{} likes to eat {} ".format(self.first, food)
        
    def birthday(self,age):
        return "Happy {}th birthday of {}".format(age, self.first)

user1 = User("Anik","Barua",15)
print(user1.full_name())
print(user1.initials())
print(user1.likes("Pizza"))
print(user1.birthday(27))




# Experimenting class attributes 

class User: 
    active_users = 0 # Class attribute
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last 
        self.age = age 
        User.active_users += 1 # Class attribute  - User class 
        
    def full_name(self):
        return "First name: {}, Last name: {}".format(self.first, self.last)
        
    def logout(self):
        User.active_users -= 1 # Class attribute
        return "Number of active user: {}".format(User.active_users) 
    

user1 = User("Anik","Barua",15)
user2 = User("Lingling","Xue",20)
print(User.active_users)
print(user1.full_name())
print(user2.logout())



# Class attributes 

class Pet: 
    
    allowed = ["dog","fish","cat","cow"]
    
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise valueError("Cant be accepted as pet ") 
        
        self.name = name
        self.species = species
        
    def set_species(self, species):
        if species not in Pet.allowed:
            raise valueError("Cant be accepted as pet ") 
        self.species = species
    
    
animal1 = Pet("Gheu gheu","dog")
animal2 = Pet("Miao","cat")

print(id(Pet.allowed))    
print(Pet.allowed)
print(id(animal1.allowed))    
print(animal1.allowed)
print(id(animal2.allowed))    
print(animal2.allowed)



# Instance method 

class Sum: 
    def add_number(self,x,y):
        return (x+y)

# each of the objects have their own copy of the method shown in the class
# this is called instance method 
object1 = Sum()
object2 = Sum()

print(object1.add_number(1,2))
print(object2.add_number(3,4))



# Instance, class and static method 
from math import pi

class Pizza:
    total_count = 0 # class variable
    
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cooked = False
        self.increment_total()
    #Instance method - we need to pass a reference     
    def cook(self):    
        self.cooked = True
        print("Cooking with ingrediants {}".format(self.ingrediants))
    
    @classmethod
    def increment_total(cls):
        cls.total_count += 1 
        
    @staticmethod
    def cal_area(radius):
        return pi * radius**2
    
p = Pizza(['cheese','tomato'])  

print(Pizza.cook is p.cook) #False
    


    
