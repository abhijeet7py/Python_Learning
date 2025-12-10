# str = input("Enter a string: ")

# # 1. using slicing method
#
# if str == str[::-1]: # Reverse using slicing and compare with original
#     print(f"{str} is a palindrome.")
#
# else:
#     print(f"{str} is not a palindrome.")

# 2. Using 2 pointer method (Without a built-in method)

str = input('Enter a string: ')

left = 0
right = len(str) - 1

while left < right:
    if str[left] != str[right]:
        print("Not a palindrome.")

    left += 1
    right -= 1
else:
    print(f"{str} is a palindrome.")

