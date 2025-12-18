n = int(input("Enter a number: "))

# 1. using for loop

if n <= 1: # prime number starts from 2 so check if n is 1 or < 1.1
    print("Not a Prime Number")

for i in range(2, n): # checks divisibility upto n-1
    if n % i == 0: # if number is divisible by any value other than 1 and itself
        print("Not a Prime Number")
        break # stops immediately after factor is found
    else:
        print("Prime Number")

# 2. Square root logic

if n <= 1:
    print("Not a Prime Number")
else:
    is_prime = True  # assuming value as prime number.

    for i in range(2, int(n ** 0.5)+ 1): # checks upto square root only
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


# 3. Using while loop

if n <= 1:
    print("Not a Prime Number")
else:
    i = 2
    while i < n:
        if n % i == 0:
            print("Not a Prime Number")
            break
        i += 1
    else:
        print("Prime Number")
