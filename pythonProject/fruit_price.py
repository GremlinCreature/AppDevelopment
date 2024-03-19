def fruit_price(**kwargs):
#definiting the function that accepts dictionaries
    sum=0
#establishing sum value
    for i in kwargs.values():
#repeat for each value in dictionary
        sum=sum+i
#adds values to a sum
    return sum
k=fruit_price(mango=10,apple=5,orange=15)
print(k)