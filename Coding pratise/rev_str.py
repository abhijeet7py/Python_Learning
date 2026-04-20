str1 = "Automation"

# Slicing method

rev_str = str1[::-1]
print(rev_str)

# Using for loop
rev = ""
for ch in rev_str:
    rev += ch

print(rev)

# Using while loop

rev1 = ""
i = len(str1) - 1

while i >= 0:
    rev1 += str1[i]
    i -= 1

print(rev1)

