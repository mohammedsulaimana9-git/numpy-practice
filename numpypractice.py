import numpy as np
"""#one dimensional array
arr = np.array([1,2,3])
print(arr)


#two dimensional array
arr2 = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr2)

#Creating arrays with Default value 
#zeros function
arr3 = np.zeros((2,2))
print(arr3)

#once function 
arr4 = np.ones((2,2))
print(arr4)

#Creating array with specific function 
arr5 = np.full((2,2), 2)
print(arr5)
arr6 = np.full((4,4),4)
print(arr6)

#Creating identity matrix
arr7= np.eye(4)
print(arr7)
arr8 = np.eye(10)
print(arr8)

#Creating sequence of numbers in numpy
arr9 = np.arange(1,10,1)
print(arr9)






#ATTRIBUTES 

#Array shape
arr10 = np.array([[1,2,3],
                 [2,3,3]])
print(arr10.shape)

#Array size 
print(arr10.size)

#Array dimensions
print(arr10.ndim)

#data type 
print (arr10.dtype)

#item size
print(arr10.itemsize)

#change data type
print(arr10.astype(str))
print(arr10.dtype)

#Mathematical functions which can be performed on numpy arrays

arr11= np.array([10,20,30])
print(arr11 + 5)
print(arr11 * 5)
print(arr11 / 5)

#Aggregation function 
arr12 = np.array([1,2,3,4,5])

print(np.sum(arr12))
print(np.mean(arr12))
print(np.min(arr12))
print(np.max(arr12))
print(np.var(arr12))
print(np.std(arr12))

arr13 = np.array([10,20,30,40,50])
print(arr13[::-1]) #slicing
print(arr13[[0,2,4]])#Fancy indexing

#Boolean Masking
arr14 = np.array([10,20,30,40,50])
mask = arr14>25
print(mask)
print(arr14[mask])

print(arr14[arr14>23])

#Reshaping

arr15 = np.array([1,2,3,4,5,6])
arr1 = arr15.reshape(2,3)
print(arr1)
arr2 = arr15.reshape(3,2)
print(arr2)
arr3 =arr2.reshape(-1)
print(arr3)

#Inserting elemenst in an array
arr = np.array([10,20,30,40,50])
arr2 = np.insert(arr,1,200)
print(arr2)

#Inserting an element in the row
arr = np.array([[1,2],[3,4]])
print(arr)
arr2 = np.insert(arr,1,[5,6] , axis =1)
print(arr2)

#Appending
arr = np.array([[1,2],[3,4]])
print(arr)
arr2 = np.append(arr,[[5],[6]], axis=1)
print(arr2)

#Concatenation 
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a,b), axis =1))"""

#Np split
arr = np.array([10,20,30,40])
print(np.split(arr,2))















