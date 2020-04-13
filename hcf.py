def hcf(n1,n2):
  if(n2!=0):
    hcf(n2,n1%n2)
    return n1

x=56
y=7
res=hcf(x,y)
print(res)


def LargestDigits(n):
  largest=0
  smallest=9
  r=0
  while(n!=0):
    r=n%10
    largest=max(r,largest)
    smallest=min(r,smallest)
    n=n//10
  print(largest)
  print(smallest)
#calling largestDigits function
LargestDigits(6789)


