student_name=[]
student_age=[]
# creating arrays
while len(student_name)<7 and len(student_age)<7:
    student_name.append(input("Input student name: "))
    student_age.append(input("Input student age: "))
#inputting 7 names and ages
print(student_name)
print(student_age)
for i in range(0, len(student_name), 1):
    print(student_name[i], student_age[i])
#printing out names with corresponding ages
for i in student_age:
    if int(i)>20:
      print(i)
#printing all ages bellow 20 , i guess ?