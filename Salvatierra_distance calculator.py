# Jaydiel Rain S. Salvatierra
# Create calucatar
# Distance is calucatar

import math

x1 = int(input("Enter first number: "))
y1 = int(input("Enter first number: "))

x2 = int(input("Enter second number: "))
y2 = int(input("Enter second number: "))

distance = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))

print(f"The distance between {x1}-{x2} and {y1}-{y2} is {distance:.2}")

# Ending ===============================================================