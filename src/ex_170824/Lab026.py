# Write a Python program to calculate the
# area of circle given its radious using the formula
# area = pi x r^2 (take pie as 3.14)
import math

# Logic building formula

# Step1: Figure out the inputs and outputs
# input -> r -> data type -> float
# pi -> 3.14
# power -> pow or ** -> any

# o/p -> float - area, print area

# step 2:
# rough logic = area = 3.14 * pow(r,2)

# step 3: Write the logic

radious = float(input("Enter the radious of the circle:"))
print(radious)
area = math.pi * math.pow(radious,2)
print(f"Area of circle is {area:.2f}")

# * -> Multiplication
#
# **--> Power
print(3.14159*(float(input("Enter the radious:"))**2))


















