import numpy as np

def unique(lis1t):
  unique_list=[]
  for x in list1:
    if x not in unique_list:
      unique_list.append(x)
  for x in unique_list:
    print(x)

def unique1(list1):
  list_set=set(list1)
  unique_list=(list(list_set))
  for x in unique_list:
    print (x)

def unique2(list1):
  x=np.array(list1)
  print(np.unique(x))


#main Code
list1 = [10, 20, 10, 30, 40, 40] 
print("Append Method")
unique(list1)
print("Using Set Method")
unique1(list1)
print("Using Numpy")
unique2(list1)