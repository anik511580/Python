
# Half pyramid print 

print("Half pyramid * print")

for i in range (0, 5): # i = 0, 1, 2, 3, 4
    for j in range(0, i+1): # The last range will be i+1=4+1=5 
        print("*", end=" ")
    print("")


# Half piramid print    

print("Half pyramid number print")

for i in range (0, 5): # i = 0, 1, 2, 3, 4
    for j in range(0, i+1): # The last range will be i+1=4+1=5 
        print( j+1, end=" ")
    print("")


# Half pyramid print i 

print("Print i for exactly 10 number")

for i in range (10): # i = 0,1,2,3,4,5,6,7,8,9
    for j in range(i+1): # 
        print(i, end=" ")
    print("")
    

# Half pyramid print j 

print("Print j for exactly 10 number")

for i in range (10): # i = 0,1,2,3,4,5,6,7,8,9
    for j in range(i+1): 
        print(j, end=" ")
    print("")


# Sqared value of pyramid 

print("Print square value of exactly 10 number")

for i in range (10): # i = 0,1,2,3,4,5,6,7,8,9
    for j in range(i+1): 
        print(j**2, end=" ")
    print("")



