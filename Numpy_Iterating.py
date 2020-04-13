import numpy as np
arr=np.arange(12)
arr=arr.reshape(3,4)
print("Original Array:")
print(arr)
print("Modified Array:")
# iterating Array
for i in np.nditer(arr):
  print(i,end=" ")

#transpose of an Array
print("Transpose: ")
b=arr.T
for i in np.nditer(b):
  print(i,end=" ")
print("Modified Array: ")
for x in np.nditer(arr, op_flags = ['readwrite']):
    x[...] = 5*x
print('Modified array is:')
print(arr)

print('External Loop:') 
for x in np.nditer(arr,flags=['external_loop'] ,order = 'C'):
    print(x)

# iterating array using f_index 
# parameter
print("iterating array using f_index ")
it = np.nditer(arr, flags=['f_index'])
while not it.finished:
      print("%d <%d>" % (it[0], it.index), end=" ")
      it.iternext()

print("Broadcasting Iteration:")
arr1=np.array([12,45,76,87])
print('Modified array is:')
for x,y in np.nditer([arr,arr1]): 
    print("%d:%d" % (x,y))

