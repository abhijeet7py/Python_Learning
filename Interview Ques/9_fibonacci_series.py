n = int(input("Enter no of terms: ")) # takes user input


# 1. using for loop
# a, b = 0 , 1 # initialize first two fibonacci numbers
#
# print(a, b, end= " ") # print the numbers, end = " " ensure they printed in same line
#
# for i in range(2, n):
#     c = a + b
#     print(c, end = " ")
#     a = b
#     b = c

# 2. Using while loop

# a, b = 0 ,1
#
# count = 0 # count variable to keep track of how many terms we have printed
#
# while count < n:
#     print(a, end = " ")
#     a , b = b, a + b
#     count += 1


# 3. Using Recursion

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter no of terms: "))

for i in range(n):
    print(fibo(i), end=" ")



