s = "I love Automation testing"

# 1. Using slicing and Split method

words = s.split()

rev = " ".join(words[::-1])
print(f"Reversed Str: {rev}")

# 2. Using for loop

word = s.split()
revs = ""

for i in range(len(word)-1, -1, -1):
    revs += word[i] + " "

print(f"Reversed Str: {revs}")