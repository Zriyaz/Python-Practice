
import array 
import numpy as np
print("Array Creation using List")
arr=[1,2,3,4,5]
for i in arr:
	print(i)

arr=array.array('i',[6,7,8,9])
for i in range(len(arr)):
  print(arr[i],end=" ")
print("\r")

matrix=np.empty(2,dtype=int)
print("Matrix : ",matrix)

matrix1=np.empty([2,2],dtype=int)
print("Matrix1: ",matrix1)
matrix2=np.empty([3,3])
print("matrix2: ",matrix2)

b = np.zeros(2, dtype = int)
print("Matrix b : \n", b)
a = np.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", a)
 
c = np.zeros([3, 3])
print("\nMatrix c : \n", c)

myarray=np.arange(8)
print(myarray)

myarray=np.arange(8).reshape(2,4)
print("Rearrange MyArray",myarray)
myarray=np.arange(8).reshape(2,4)
print(myarray)
myarray=np.arange(8).reshape(4,2)
print(myarray)
myarray=np.arange(8).reshape(2,2,2)
print(myarray)


print("A\n", np.arange(4).reshape(2, 2), "\n")
 
print("A\n", np.arange(4, 10), "\n")
 
print("A\n", np.arange(4, 20, 3), "\n")

# restep set to True
print("B\n", np.linspace(2.0, 3.0, num=5, retstep=True), "\n")
 
# To evaluate sin() in long range 

x = np.linspace(0, 2, 10)
print("A\n", np.sin(x))


