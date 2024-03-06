m1=float(input("Input first mark"))
m2=float(input("Input second mark"))
m3=float(input("Input third mark"))
m4=float(input("Input fourth mark"))
sc=(m1+m2+m3+m4)/4
if sc>100 or sc<0:
    print("Invalid range")
elif sc>=80:
    print("A")
elif sc>=60:
    print("B")
elif sc>=50:
    print("C")
else:
    print("Fail")
