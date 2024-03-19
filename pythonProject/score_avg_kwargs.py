def marks_avg(**marks):
    sum=0
    for i in marks.values():
        sum=sum+i
    avg=sum/len(marks)
    return avg
print(marks_avg(IT5014=60, IT7809=80, IT6798=50, IT5048=70))