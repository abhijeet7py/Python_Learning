# - Write a Python program to calculate the area
# of a circle given its radius using the formula ```
# area=π×r^2``` ( Take pie as 3.14)

import math
radious = float(input("Enter the radious of the circle:"))
print(radious)
area = math.pi * math.pow(radious,2)
print(f"Area of circle is {area:.2f}")

# * -> Multiplication
#
# **--> Power
print(3.14159*(float(input("Enter the radious:"))**2))