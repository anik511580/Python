from __future__ import print_function
import numpy as np 


#Create n-dimentional array 

#1D array
data_1 = [1,2,3,4,5]
arr1 = np.array(data_1)
print("1D array: ", arr1)



#2D array
data_2 = [range(1,5), range(5,9)] 
arr2 = np.array(data_2) 
print("2D array: ", arr2) #[[1 2 3 4] [5 6 7 8]]
print("2D array as list:  ", arr2.tolist()) #[[1 2 3 4], [5 6 7 8]]


#3D array
data_3 = [range(1,5), range(5,9), range(9,13)] 
arr3 = np.array(data_3) 
print("3D array: ", arr3) 
print("3D array as list ", arr3.tolist()) 




#Create Special array 



print("np.zeros(10): ",np.zeros(10)  )
print("np.zeros((3,6))", np.zeros((3,6)))
print("np.ones(10): ", np.ones(10)  )
print("np.linspace(0,1,5): ",np.linspace(0,1,5))
print("np.logspace(0,3,4): ",np.logspace(0,3,5))



int_array = np.arange(5)
print("int_array = ", int_array)
print("float_array = ",int_array.astype(float))

#using range
for i in range(0,5):
    print(i)


#Examining array: 


print("arr1.dtype:  ", arr1.dtype) 
print("arr2.dtype:  ", arr2.dtype) 
print("arr2.dim:  ", arr2.ndim) 
print("arr2.shape:  ", arr2.shape) 
print("arr3.shape:  ", arr3.shape) 


print("ar2: ", arr2)
print("arr2.size: ", arr2.size)
print("len(arr2): ", len(arr2))



# Reshaping 


arr = np.arange(10, dtype = float).reshape((2,5))
print("arr: \n", arr)
print("arr.shape: \n ", arr.shape)
print("arr.reshape: \n ", arr.reshape(5,2))



# Reshaping 


a = np.array([0,1,2,3,4])
print("a:", a)
a_col  = a[:,np.newaxis]
print("a_col: ", a_col)

a_col = a[:,None]
print("a_col: ", a_col)

#Transpose 
print("Transpose: ", a_col.T)


# Flatten:  always return a flat copy of the original array 

print("Flatten output: ")
print("arr: ", arr)

arr_flt = arr.flatten()
arr_flt[0] = 33 # add 33 in the 0th index

print("arr_flt: ", arr_flt)
print("arr: ", arr)

# Ravel: return a value of the original array 

print("Ravel output: ")
arr_flt2 = arr.ravel()
arr_flt2[0] = 33
print("arr_flt2: ", arr_flt2)
print("arr ", arr)