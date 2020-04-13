import numpy as np

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
#print(list1*list2) give error

arr1=np.array(list1)
arr2=np.array(list2)
print(arr1*arr2)

#indexing
a=np.arange(10,1,-2)
print("\n A sequential array with a negative step: \n",a)
newarr=a[np.array([3,1,2])]
print("\n Elements at these indices are:\n",newarr)
newarr1=a[np.array([4,-3,0])]
print("Elements are:",newarr1)

#Basic Slicing and indexing  
'''Consider the syntax x[obj] where x is the array and obj is the index.
a slice object that is of the form start : stop : step
an integer
or a tuple of slice objects and integers
'''
newarr2=np.arange(20)
print("\n Array is:\n ",newarr2)

# newarr2[start:stop:step]
print("\n newar2[-8:17:1]  = ",newarr2[-8:17:1]) 
# The : operator means all elements till the end.
print("\n newarr2[10:]  = ",newarr2[10:])
