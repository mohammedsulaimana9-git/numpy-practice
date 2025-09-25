import numpy as np
#one dimensional array
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


