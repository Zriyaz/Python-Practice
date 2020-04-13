import numpy as np

#numpy.lower() String 
string=np.char.lower(['KONGU' ,'ENGINEERING','COLLEGE'])
STRING=np.char.upper(['kongu' ,'engineering','college'])
print(string)
print(STRING)
# splitting a string
print(np.char.split('md,riyaz,ansari'))

# splitting a string
print(np.char.join('-', 'riyaz'))
 
# splitting a string
print(np.char.join(['-', ':'], ['ansari', 'md']))

a=np.array(['geeks', 'for', 'geeks'])
# counting a substring
print(np.char.count(a,'geek'))
 
# counting a substring
print(np.char.count(a, 'fo'))

a=np.array(['geeks', 'for', 'geeks'])
 
# counting a substring
print(np.char.rfind(a,'geek'))
 
# counting a substring
print(np.char.count(a, 'fo'))

print(np.char.isnumeric('riyaz'))
 
# counting a substring
print(np.char.isnumeric('12ansari'))

# comparing a string elementwise
# using equal() method
a=np.char.equal('riyaz','ansari')
print(a)

# comparing a string elementwise
# using greater() method
a=np.char.greater('geeks','for')

# comparing a string elementwise
# using unequal() method
a=np.char.unequal('kazmi','md')
print(a)
