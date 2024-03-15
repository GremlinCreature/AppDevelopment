def sum_all():
    nums=[]
    number_sum=0
    num_total=int(input("Input total amount of numbers you'd like to put in: "))
    for i in range(num_total):
        num=(int(input("Input a number: ")))
        nums.append(num)
    for i in nums:
        number_sum=number_sum+i
    return number_sum
print(sum_all())



