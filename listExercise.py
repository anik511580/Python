#Nested List programs:

nums = [1,2,3]

print([(x+2) for x in nums])


numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)


name ="anik the great"

print([char.upper() for char in name])


print([num*10 for num in range(1,11)])

print(bool(""))
print(bool(" "))
print(bool(0))

print([bool(val) for val in [0, [], [""], [" "],[''], [' ']]])


numberList = [1,2,3,4,5,6]
print("Number List: ", numberList)
stringList = [str(n) for n in numberList]
print("String List: ", stringList)


evenList = [num for num in numberList if num%2 == 0 ]
print("Even List: ", evenList)
oddList = [num for num in numberList if num%2 != 0]
print("Odd List: ", oddList )

print([num*2 if num%2==0 else num/2 for num in numberList])

with_vowels = "This is so much fun man!"
print([char for char in with_vowels if char not in "aeiou"]) #without join
print(''.join(char for char in with_vowels if char not in "aeiou")) #with join

print(''.join(["anik","is","the", "best"])) #join without space 
print(' '.join(["anik","is","the", "best"])) #join with a space 
print('...'.join(["anik","is","the", "best"])) #join with some dots 

answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]#intersection
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

answer = [num for num in range(1,101) if num%12 == 0  ] # list which can be devided by 12 

answer = [char for char in "amazing" if char not in "aeiou"] 



#Nested Comprehension programs:



nestedList= [[1,2,3],[4,5,6],[7,8,9]]
#first access the out list, and then inside of that list 
print(nestedList[0][1]) # Output:2
print(nestedList[-1]) # Output: [7,8,9]
print(nestedList[-1][-1]) # Output: 9


for l in nestedList:# to access the first level/items
    for value in l:# to access the value of that item
        print(value) # Output: 1,2,3,4,5,6,7,8,9
        
[[ print(value) for value in l] for l in nestedList] # Output: 1,2,3,4,5,6,7,8,9

board = [num for num in range(1,4)]
print("board value: ", board)
board = [[num for num in range(1,4)] for value in range(1,4)]
print("new board value: ", board)
print( [["X" if num%2==0 else "0" for num in range(1,4)] for value in range(1,4)] )



answer = [[x for x in range(0,3)] for num in range(0,3)]
print(answer)

#10x10 matrix 
newAnswer = [[x for x in range(0,10)] for num in range(0,10)]
print(newAnswer)

