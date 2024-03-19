def fruit_price(**kwargs):
    sum=0
    for i in kwargs.keys():
        print(i)
    print(kwargs.keys())
    return
fruit_price(mango=10, apple=5, orange=15)
