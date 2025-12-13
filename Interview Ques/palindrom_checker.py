# str = input("Enter a string: ")

# # 1. using slicing method
#
# if str == str[::-1]: # Reverse using slicing and compare with original
#     print(f"{str} is a palindrome.")
#
# else:
#     print(f"{str} is not a palindrome.")

# 2. Using 2 pointer method (Without a built-in method)

s = input("Enter a string: ").lower().split()

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print(f"{s} is a palindrome.")


