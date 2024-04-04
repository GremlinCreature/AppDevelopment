def marks(*marks):
    all=0
    for i in marks:
        all=all+i
    avg=all/len(marks)
    return avg

avg=marks(100,100,78,98,100,76,87,90,100,100,100)
print("Average score is: ", avg)
if avg<50:
    print("Fail")
elif avg>=50 and avg<60:
    print("Pass")
elif avg>=60 and avg<70:
    print("Second class lower")
elif avg>=70 and avg<90:
    print("Second class upper")
elif avg>=90:
    print("First class")