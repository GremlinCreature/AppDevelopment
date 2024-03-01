import math
# import math module
x1 = input("Input first value")
x2 = input("Input second value")
y1 = input("Input third value")
y2 = input("Input fourth value")
# read values for calculations
xx = float(x2)-float(x1)
yy = float(y2)-float(y1)
xx2 = xx**2
yy2 = yy**2
xy = xx2+yy2
d = math.sqrt(xy)
print(d)