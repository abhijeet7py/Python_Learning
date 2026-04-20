# Checking if a string is a palindrom or not

# 1. Using Slicing method

str1 = input("Enter a String: ")

if str1 == str1[::-1]:
    print(f"{str1} is a palindrome.")

else:
    print(f"{str1} is not a palindrome.")