def student_numb ():
    nmbrs=int(input("Input the total number of students: "))
    student={}
    for i in range(nmbrs):
        student[input("Input student number: ")]=input("Input student name: ")
    return student
print(student_numb())