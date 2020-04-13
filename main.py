import numpy as np
arr=np.array([1,2,3])
print(arr)

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
arr=np.array((1,2,3))
print(arr)

matrix1=np.array([[3,4],[6,7]])
matrix2=np.array([[8,9],[4,5]])
print("Add")
sum1=np.add(matrix1,matrix2);

print("Numpy")

print(matrix1 + 2)
print("Sum : ",matrix1.sum())
print(matrix1+matrix2)
print(matrix1.dtype)

string=np.array(['a','b'])
print(string.dtype)
arr1=np.array([[4,7,],[2,6]],dtype=np.float64)
arr2=np.array([[3,6],[2,8]],dtype=np.float64)
sum1=np.add(arr1,arr2);
print("Addition of Two Matrix")
print(sum1)
print(arr1+arr2)
print(arr1)
print(np.sum(arr1))
print(arr2)
print(np.sum(arr2))
print("Square")
print(np.sqrt(arr1))
print("Transpose")
print(arr2.T)



