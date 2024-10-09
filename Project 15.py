import math
radius = int(input("Please enter the radius of the circle:"))
def caculate(radius):
    circumfrince = 2 *math.pi * radius
    return circumfrince


result = caculate(radius)
print(result)