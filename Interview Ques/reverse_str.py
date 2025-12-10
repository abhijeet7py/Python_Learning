str1 = "Automation"

# 1. Using Slicing method

rev = str1[::-1] # [start:stop:step] using -1 step reverses the string
print(rev)

# 2. Using Reversed method

rev = "".join(reversed(str1)) # reversed() returns an iterator: join() converts back it to string.
print(rev)

# 3. Using for loop
str1 = "Automation"
rev = ""
for char in str1:
    rev = char + rev

print(rev)

# 4. Using while loop
str1 = "Automation"
rev = ""

i = len(str1) - 1

while i >= 0:
    rev = rev + str1[i]
    i -= 1

print(rev)
