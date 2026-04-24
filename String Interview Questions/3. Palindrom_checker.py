s = input("Enter a word: ")

# 1. Using slicing
if s == s[::-1]:
    print(f"{s} is a palindrome")

else:
    print(f"{s} is not a palindrome")

# 2. using 2 Pointer approch

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print(f"{s} is not a palindrome")
        break
    left += 1
    right -= 1

else:
    print(f"{s} is a palindrome")


# 3. Defining func and ignoring case and spaces

s1 = "A man a plan a canal Panama"
def ispalindrome(s1):
    filtered = ""

    for ch in s1:
        if ch.isalnum():
            filtered += ch.lower()

    left, right = 0, len(filtered) -1

    while left < right:
        if filtered[left] != filtered[right]:
            print(f"{s1} is not a palindrome")
            break
        left += 1
        right -= 1
    else:
        print(f"{s1} is a palindrome")


ispalindrome(s1)










