n = int(input("Enter a number: "))

total = 0

while n > 0:
    total += n % 10
    n = n // 10

print("The sum of the digits is", total)