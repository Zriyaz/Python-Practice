
#8. program to convert floating to binary

def floatoctal_convert(my_number, places = 3):
   my_whole, my_dec = str(my_number).split(".")
   my_whole = int(my_whole)
   my_dec = int (my_dec)
   res = bin(my_whole).lstrip("0b") + "."
   for x in range(places):
      my_whole, my_dec = str((my_decimal_converter(my_dec)) * 8).split(".")
      my_dec = int(my_dec)
      res += my_whole
   return res
def my_decimal_converter(num):
   while num > 1:
      num /= 10
   return num
# Driver Code
n = input("Enter floating point value : \n")
p = int(input("Enter the number of decimal places of the result : \n"))
print(floatoctal_convert(n, places = p))

#Find minimum sum of factors of number
def findMinSum(num): 
    sum = 0   
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num  
num = 45
res=findMinSum(num)
print(res) 


'''# 5 Program for Difference between sums of odd and even digits
num=int(input(&quot;enter number&quot;))
even=0
odd=0
while(num!=0):
    rem=int(num%10)
    if(rem%2==0):
        even=even+rem
    else:
        odd=odd+rem
    num=num/10    
diff=even-odd      
print(&quot;difference between even and odd digit &quot;+str(diff))'''


# 9 Check whether a number has consecutive 0’s in the given base or not
def hasConsecutiveZeroes(N, K): 
    z = toK(N, K) 
    if (check(z)): 
        print("Yes") 
    else: 
        print("No") 

def toK(N, K): 
    w = 1
    s = 0
    while (N != 0): 
        r = N % K 
        N = N//K 
        s = r * w + s 
        w = w*10
    return s 
def check(N):   
    fl = False
    while (N != 0): 
        r = N % 10
        N = N//10
        if (fl == True and r == 0): 
            return False
        if (r > 0): 
            fl = False
            continue
        fl = True
    return True
  
# Main code
N=int(input("Enter Any Number : "))
K= int(input("Enter Base Number : "))
hasConsecutiveZeroes(N, K) 



# 3. print the numbers from 10 to 1 in the descending order
n=int(input("Enter Number :"))
i=n;
while(i>=0):
   print(i, end=" ")
   i=i-1


# 4 Program for Sum of squares of first n natural numbers
n=int(input("Enter number for square "))
b=0
for i in range(1,n+1):
    t=0
    t=i*i
    b=t+b


print(b)


# 1 Program to perform Arithmetic operations (add,sub,mul,div) using complex datatypes
a=complex(input("enter first complex number "))
b=complex(input("enter second complex number "))
ch=input("Enter the operator for operation +,-,*,/ ")
if ch=='+':
      print("add of two complex number is ",a+b)
elif ch=='-':
      print("Sub of two number is ",a-b)
elif ch=='*':
      print("Multiply of two number is ",a*b)
elif ch=='/':
      print("Division of two number is ",a/b)



# 2 Program to print ASCII Value of a character
a=input("Enter character for ascii ")
print(ord(a))

#10Python Program - Check Alphabet or Not
print("Enter '0' for exit.");
ch = input("Enter any character: ");
if ch == '0':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print(ch, "is an alphabet.");
    else:
    	print(ch, "is not an alphabet.");

#11. write a program to accepting only number as input
def Survey():

    print('1) Blue')
    print('2) Red')
    print('3) Yellow')

    while True:
        try:
            question = int(input('Out of these options\(1,2,3), which is your favourite?'))
            break
        except:
            print("That's not a valid option!")

    if question == 1:
        print('Nice!')
    elif question == 2:
        print('Cool')
    elif question == 3:
        print('Awesome!')
    else:
        print('That\'s not an option!')

Survey()
