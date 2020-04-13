import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print(arr)
arr=np.array((1,2,3))
print(arr)
print("basic operations on array")
print("Additing 1 to Every Elements",arr+1)
print("Subtracting 2 to Each Elements",arr-2)
print ("Multiplying each element by 10:", arr*10)
print("Squaring Each Elements",arr**2)


matrix = np.array([
  [1,2,3],
  [4,5,6],
  [7,8,9]])
print("Matrix",matrix)
print("Largest Element:",matrix.max())
print ("Row-wise maximum elements:",matrix.max(axis=1))
print ("Column-wise minimum elements:",matrix.min(axis=0))
print("Sum of all Elements of matrix",matrix.sum())
print ("Cumulative sum along eachrow:",matrix.cumsum(axis=1))


