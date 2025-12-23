lst = [11, 2, 3, 12, 4, 1, 5,7,76,6]

# 1. Using a new list

uniq = [] # create a list for unique elements

for i in lst: # iterate through each element form list
    if i not in uniq: # checks if i is already present in uniq list
        uniq.append(i) # not in ensures duplicates are ignored

print(uniq)

# 2. Using a set

uniq = list(set(lst)) # order cant be preserved with this method
print(uniq)

# 3. While preserving order method

seen = set() # create an empty set
uniq = [] # create a list to store unique

for i in lst: # iterate over each element
    if i not in seen:
        uniq.append(i)
        seen.add(i)

print(uniq)