# Checking if a string is a palindrom or not

# 1. Using Slicing method

str1 = input("Enter a String: ")

if str1 == str1[::-1]:
    print(f"{str1} is a palindrome.")

else:
    print(f"{str1} is not a palindrome.")

# 2 Pointer method

str1 = str1.lower().split()

left = 0
right = len(str1) - 1

while left < right:
    if str1[left] != str1[right]:
        print(f"{str1} is not a palindrom.")
        break
    left += 1
    right -= 1

else:
    print(f"{str1} is a palindrome.")
