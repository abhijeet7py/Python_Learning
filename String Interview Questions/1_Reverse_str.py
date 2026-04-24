s = "Automation"

# 1. Using Slicing

rev = s[::-1]
print(f"Reversed : {rev}")

# 2. Using for loop
revs = ""
for ch in s:
    revs = ch + revs

print(f"Reversed Str: {revs}")

# 3. Using Reversed Method

re = "".join(reversed(s))
print(f"Reversed Str: {re}")

# 4. Using while loop

r = ""
i = len(s) - 1

while i >= 0:
    r += s[i]
    i -= 1

print(f"Reversed Str: {r}")