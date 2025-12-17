n = int(input("Enter a number: "))

# 1. using a for loop

fact = 1

for i in range(1,n+1):
    fact = fact * i

print("Factorial: ", fact)