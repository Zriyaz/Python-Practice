'''Aim: Program to  perform Arithmetic operations (add,sub,mul,div) using complex  datatypes'''

#function Definition
def Sum(arr,n):
  s=0
  for i in range(n):
    s=s+arr[i]
  print(s)

def Mul(arr,n):
  s1=1
  for i in range(n):
    s1+=s1*arr[i]
  print(s1)

arr=[1,2,3,4,5]
l=len(arr)
Sum(arr,l)
Mul(arr,l)

'''2. Program to print ASCII Value of a character'''
ch=input("Enter Any Character to print ASCII : ")
print("The ASCII value of '" + ch + "' is", ord(ch)) 


'''3. print the numbers from 10 to 1 in the descending order'''

num=int(input("Enter Any Number"))
n=num
while(n >= 1):
  print(n, end = " ")
  n=n-1

''' 4.Program for Sum of squares of first n natural numbers '''

num = int(input("Enter Any Number : "))
s=0
for i in range(1,n+1):
  s = s + (i*i)
print("Sum Of Square :",s)
