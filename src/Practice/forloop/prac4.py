# Reversing a string using for loop

text = input("Enter a string: ").lower()
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)

