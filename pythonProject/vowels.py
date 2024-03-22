m=input("Input your message: ")
ml=list(m)
v=['a','e','i','o','u']
V=['A','E','I','O','U']
counter=0
for l in ml:
    for l1 in v :
        if l[0] == l1:
            counter=counter+1
    for l2 in V:
        if l[0]==l2:
            counter=counter+1
print(counter)
