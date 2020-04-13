record = int(input("Enter the student record to add :"))

stud_data={}
student={}
result=set()
for i in range(0,record):
    Name = input("Enter the student name :").split()
    course = input("Enter the {} Course :".format(Name)).split()
    Nam_key =  Name[0]
    course_value = course[0]
    stud_data[Nam_key] = {course_value}

print(stud_data)

#Searching the Result
find=input("Enter Course: ")
student=stud_data.items()
print(student)
for item in student:
  if(item[1]==find):
    result.add(item[0])
   

for item in result:
  print(item,end=" ") 
