# Jaydiel Rain S. Salvatierra
#8 adelfa
#LT1

import math

#This finds the radius of the garden
Radius = float(input("Enter the Radius of the garden"))

#This finds the area of the garden
area = math.pi * math.pow(Radius,2)

#This finds the circumference of the garden
circumference = 2 * math.pi * Radius

#This finds the square root of the garden
square_root = math.sqrt(area)

#This finds the rounded up
floor_area =  math.floor(area)

#This finds rounded down
ceil_area = math.ceil(area)

print(f"The radius of the garden is {Radius}")
print(f"The area of the garden is {area:. 2f}")
print(f"The circumference of the garden is {circumference:. 2f}")
print(f"The square root of the garden is {square_root:. 2f}")
print(f"The rounded down area of the garden is {floor_area:. 2f}")
print(f"The rounded up area of the garden is {ceil_area:. 2f}")
