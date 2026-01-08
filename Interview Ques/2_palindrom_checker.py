str = input("Enter a string: ")

# 1. using slicing method

if str == str[::-1]: # Reverse using slicing and compare with original
    print(f"{str} is a palindrome.")

else:
    print(f"{str} is not a palindrome.")

# 2. Using 2 pointer method (Without a built-in method)

s = input("Enter a string: ").lower().split() # split the string into list of words

left = 0 # points to the first word in the list
right = len(s) - 1 #points to the last word in the list

while left < right: # Loop continues until two pointers are not crossed
    if s[left] != s[right]: # compares words from beginning to end
        print("Not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print(f"{s} is a palindrome.")


