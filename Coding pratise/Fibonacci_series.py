n = int(input("Enter no of terms: "))

# Using a for loop:

a , b = 0, 1  # declaring first two fibo numbers

print(a, b, end=" ") # printing it with end= " " so that all numbers will get printed inline

for i in range(2, n): # iterating  through the terms
    c = a + b         #
    print(c, end=" ")
    a = b  # Updating the variables
    b = c


# Using while loop

a , b = 0, 1

count = 0

while count < n:
    print(a, end= "\n",)
    a , b = b, a + b
    count += 1



