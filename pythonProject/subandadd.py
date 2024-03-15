def calculator(a,b):
    add=a+b
    sub=a-b
    return add, sub
num=calculator(int(input("Input  the first number: ")), int(input("Input the second number: ")))
print(num)
print("Sum is: ", num[0])
print("Dif is: ", num[1])
