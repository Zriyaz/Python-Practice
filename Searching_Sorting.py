import numpy as np

matrix=np.array([[12,15],[10,1]])
print(matrix)
arr1=np.sort(matrix,axis=0)
print ("Along first axis : \n", arr1)        

a = np.array([[10, 15], [12, 1]])
arr2=np.sort(a,axis=-1)
print ("\nAlong first axis : \n", arr2)

a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = None)        
print ("\nAlong none axis : \n", arr1)

arr=np.array([ 9, 3, 1, 7, 4, 3, 6])
print("Original Array:")
print(arr)

b=np.argsort(arr)
print('Sorted indices of original array->', b)
c = np.zeros(len(b), dtype = int)
for i in range(0, len(b)):
    c[i]= arr[b[i]]
print('Sorted array->', c)


#numpy.lexsort() 
a = np.array([9, 3, 1, 3, 4, 3, 6])
b = np.array([4, 6, 9, 2, 1, 8, 7])
print('column a, column b')
for (i, j) in zip(a, b):
    print(i, ' ', j) 
ind=np.lexsort((b,a))
print("Sorted Indices->",ind)


#searching techinque
matrix=np.arange(12).reshape(3,4)
print("Searching Technique")
print(matrix)
print("\nMax element : ", np.argmax(matrix))
print(("\nIndices of Max element : " , np.argmax(matrix, axis=0)))
print(("\nIndices of Max element : ", np.argmax(matrix, axis=1)))

a = np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]])
b = np.count_nonzero(([[0,1,7,0,0],[3,0,0,2,19]]))
print("Number of nonzero values is :",a)
print("Number of nonzero values is :",b)