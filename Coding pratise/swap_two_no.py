a = int(input("Enter a Number: "))
b = int(input("Enter another Number: "))

# Tuple Unpack method
# print(f"Before swapping a = {a} and b = {b}")
# a, b = b , a
# print(f"After swapping a = {a} and b = {b}")

# # using a temp var
# print(f"Before swapping a = {a} and b = {b}")
# temp = a
# a = b
# b = temp
# print("After swapping: ",a , b)

# Using arithmetic operators
print("Before swapping: ",a , b)
a = a + b
b = a - b
a = a - b
print("After swapping: ",a , b)
