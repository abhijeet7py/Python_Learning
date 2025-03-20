def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

input_string = input("Enter a word or phrase: ")

if is_palindrome(input_string):
    print("String is palindrome")
else:
    print("String is not a palindrome")