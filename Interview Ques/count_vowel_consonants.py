str = "Automation testing"
str = str.lower()

vowels = 0
consonants = 0
i = 0

# 1. Using while loop
while i < len(str):
    ch = str[i]

    if ch >= "a" and ch <= "z":
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            vowels += 1
        else:
            consonants += 1

    i += 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

# 2. using for loop

vowels = 0
consonants = 0

for ch in str:
    if ch >= "a" and ch <= "z":
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            vowels += 1

        else:
            consonants += 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")


# 3. using set for faster lookup

vowels_set = {"a","e","i","o","u"}
vowels = 0
consonants = 0

for ch in str:
    if ch.isalpha():
        if ch in vowels_set:
            vowels += 1
        else:
            consonants += 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")

