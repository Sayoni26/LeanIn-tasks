#**Task 1**

#* Write a NumPy program to test whether none of the elements of a given array is zero.
#> Take user input.

#* Write a NumPy program to test whether any of the elements of a given array is non-zero.
#> Take user input.
import numpy as np
arr=np.zeros(5)
i=0
while i<5:
    n=int(input("enter the element"))
    arr[i]=n
    i+=1
count=0
for x in arr :
    if x!=0:
        count=0
    else:
        count+=1
        break
if count==0:
    print("element has no 0 element")
else:
    print("0 object present")  

#* Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
#> Predefined input can be taken.
a1=np.array([[1,3,2,4,5],[9,8,4,6,7]])
a2=np.array([[6,3,2,7,4],[9,8,4,3,2]])
print("is the two arrays equal:")
print("original:\n",a1)
print(a2)
result=np.equal(a1,a2)
print(result)
print(a1[result])
print("is element equal within the tolerance:")
print(np.allclose(a1,a2))

#* Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.

#**Input**
x = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("the element which are greater in x")
bool_x=(x>=y)
print(bool_x)
print(x[bool_x])
print("element of y which are greater or equal to x")
bool_y=(y>=x)
print(bool_y)
print(y[bool_y])

#* Write a NumPy program to create an array of all the even integers from 30 to 70.
arr=np.arange(30,70,2)
print(arr)


#* Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
arr=np.arange(0,21)
minus=arr[9:16]
minus*=-1
print(arr)

#* Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
arr=np.identity(3,dtype="int")
print(arr)

#* Write a NumPy program to compute the inner product of two given vectors.
a1=np.array([[1,2,3],[2,3,4],[9,8,7]])
a2=np.full_like(a1,6,dtype="int32")
np.reshape(a2,(3,3))
mul=np.dot(a1,a2) 
print("the iner product of two given vector:\n",mul)


#* Write a NumPy program to save a given array to a text file and load it.
#**Input**
#> A 4x3 matrix as input and when saved as text file it should have heading as 'cl1 col2 col3'
import os 
arr=np.arange(12).reshape(4,3)
print("the array which is saved",arr)
np.savetxt('text.txt',arr,fmt='%d',header='cl1 cl2 cl3')
print("the file containing the folloing is made:")
result=np.loadtxt('text.txt',dtype="int")
print(result)