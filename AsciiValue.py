#print ascii value of r character
char='r'
print(ord(char))

arr=[1,2,3,4,5,6,7,8,9]
print(sum(arr))
l=len(arr)
s=0
mx=arr[0]
for i in range(0,l):
  s=s+arr[i]
print(s)
for j in range(0,l):
  if(arr[i]>mx):
   mx=arr[i]
print(mx)