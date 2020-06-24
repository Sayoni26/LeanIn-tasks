#**Task 2**

#* Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.

#**Expected Output:**

#**Original array:**

#[[10 40]
#[30 20]]

#**Sort the array along the first axis:**

#[[10 20]
#[30 40]]

#**Sort the array along the last axis:**

#[[10 40]
#[20 30]]

#**Sort the flattened array:**

#[10 20 30 40]

import numpy as np
arr=np.array([[10,40],[30,20]])
print("sorting along first axis:")
print(np.sort(arr,axis=0))
print("sorting alomg last axis")
print(np.sort(arr,axis=1))
print("sort the flattered array")
narr=arr.flatten('F')
print(np.sort(narr))

#* Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort the array on height.

#**Sample Output:**

#**Original array:**

#[(b'James', 5, 48.5 ) (b'Nail', 6, 52.5 ) (b'Paul', 5, 42.1 ) (b'Pit', 5, 40.11)]

#**Sort by height**

#[(b'Pit', 5, 40.11) (b'Paul', 5, 42.1 ) (b'James', 5, 48.5 ) (b'Nail', 6, 52.5 )]

dtype=[('name','S15'),('class',int),('hight','f')]
std_details=[('James', 5, 48.5 ),('Nail', 6, 52.5 ) ,('Paul', 5, 42.1 ) ,('Pit', 5, 40.11)]
struct=np.array(std_details,dtype=dtype)
print("the list entered:")
print(struct)
print("data type of the element :")
print(struct.dtype) 
new_struct=np.sort(struct,order='hight')
print(new_struct)


