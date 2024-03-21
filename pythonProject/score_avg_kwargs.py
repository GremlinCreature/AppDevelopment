def marks_avg(**marks):
    sum=0
    try:
        for i in marks.values():
            sum=sum+i
    except TypeError:
        return "Please, input only numbers."
    avg=sum/len(marks)
    return avg
print(marks_avg(IT5014=60, IT7809="k", IT6798=50, IT5048=70))