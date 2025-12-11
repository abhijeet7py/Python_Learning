a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# 1. Tuple Unpacking method

print("Before swapping: ",a , b)

a, b = b, a # 

print("After swapping: ",a , b)

# 2. Using temp variable
print("Before swapping: ",a , b)
temp = a # stores a value
a = b  # value of a is assigned to b
b = temp # get a's value from temp

print("After swapping: ",a , b)

# 3. Using Arithmatic operators

print("Before swapping: ",a , b)

a = a + b # ex. 10 + 20 = 30
b = a - b # 30 - 20 = 10
a = a - b # 30 - 10 = 20

print("After swapping: ",a , b)