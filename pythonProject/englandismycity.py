city=[]
while len(city)<5:
    city.append(input("Input name of a city: "))
print(len(city))
print(city)
city.append("Hong")
del city[0]
print(city)
city.reverse()
print(city)
