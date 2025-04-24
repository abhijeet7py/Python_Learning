# Find the largest number among three input numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

print(largest)