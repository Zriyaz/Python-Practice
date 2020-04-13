import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
print("Array Type :",type(arr))
print("No. of Dimention",arr.ndim)
print("Shape of Array", arr.shape)
print("Size of Array",arr.size)
print("Array Stores element of Type ",arr.dtype)

print("array creation techniques")
arr=np.array([[1,2,3],[4,5,6]], dtype ='float')
print("Array created using passed list:\n",arr)

arr1=np.array((1,2,3))
print("\nArray created using passed tuple:\n",arr1)

# Creating a 3X4 array with all zeros
c = np.zeros((10, 20))
print("\nAn array initialized with all zeros:\n",c)

# Create a constant value array of complex type
Complex=np.full((3,3),6,dtype='complex')
#An array initialized with all 6s Array type is complex
print(Complex)

