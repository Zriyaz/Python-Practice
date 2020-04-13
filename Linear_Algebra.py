import numpy as np
from numpy import linalg as lin

matrix=np.array([[6, 1, 1],
[4, -2, 5],
[2, 8, 7]])
print("Original Matrix: ")
print(matrix)

print("Rank of A:", np.linalg.matrix_rank(matrix))
print("\nTrace of A:", np.trace(matrix))
print("\nDeterminant of A:", np.linalg.det(matrix))
print("\nInverse of A:\n", np.linalg.inv(matrix))
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(matrix, 3))

# Python program explaining
# eigh() function

a = np.array([[1, -2j], [2j, 5]])
c, d = lin.eigh(a)
print("Eigen value is :", c)
print("Eigen value is :", d)

# Creating an array using diag 
# function
a = np.diag((1, 2, 3))
 
print("Array is :",a)
 
# calculating an eigen value
# using eig() function
c, d = lin.eig(a)
 
print("Eigen value is :",c)
print("Eigen value is :",d)

product = np.dot(5, 4)
print("Dot Product of scalar values  : ", product)
 
# 1D array
vector_a = 2 + 3j
vector_b = 4 + 5j
 
product = np.dot(vector_a, vector_b)
print("Dot Product  : ", product)

vector_a = 2 + 3j
vector_b = 4 + 5j
 
product = np.vdot(vector_a, vector_b)
print("Dot Product  : ", product)

a = np.array([[1, 2], [3, 4]])
 
# Creating an array using array
# function
b = np.array([8, 18])
print(("Solution oflinear equations:",np.linalg.solve(a, b)))

A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
 
print(("\nDeterminant of A:", np.linalg.det(A)))

print("\nTrace of A:", np.trace(A))



