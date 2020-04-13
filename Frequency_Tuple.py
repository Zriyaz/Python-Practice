
def count(tup,key):
  cnt=0
  for i in tup:
    if(i==key):
      cnt+=1
  return cnt

def countall(tup):
  cnt=0
  for i in tup:
    cnt=count(tup,i)
    print("No.Of Count",i,cnt)

def divide(tup):
  for i in tup:
    if(tup[i]%4==0 or tup[i]%8==0):
      print("Divisible by 8 and 4 : ",tup[i])
#main Code
arr=(3,4,4,5,6,7,7,8,5,7,8,8,9)
res=0;
n=0
for i in arr:
  print(arr.index(i),i)

countall(arr)
divide(arr)






  