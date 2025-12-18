n = int(input("Enter a number: "))

# 1. using a for loop

fact = 1

for i in range(1,n+1):
    fact = fact * i

print("Factorial: ", fact)

# 2. Using a while loop

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial: ", fact)

# 3. Using Recursive function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number: "))
print("Factorial: ",factorial(n))