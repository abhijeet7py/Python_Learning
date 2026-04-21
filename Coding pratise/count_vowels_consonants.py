s = "Automation Testing is good"
s = s.lower()

# Using dict freq.
vowels = {}
consonants = {}

for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            vowels[ch] = vowels.get(ch, 0) + 1

        else:
            consonants[ch] = consonants.get(ch, 0) + 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
