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
    rev = char + rev # itr 1:  = A +
                     # itr 2: A = u + A
                     # itr 3: uA = t + uA and so on

print(rev)

# 4. Using while loop
str1 = "Automation"
rev = ""

i = len(str1) - 1  # defined i since indexing starts from 0

while i >= 0: # continue loop till i is valid
    rev = rev + str1[i] # itr1:  =  + n
    i -= 1              # itr2: n= n + o

print(rev)
