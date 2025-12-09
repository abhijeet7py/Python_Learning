# Write a python program to find duplicate characters in the list

lis = ["India","is","my","country"]

str = ''.join(lis)
print(str)

duplicates = []

for char in str:
    if str.count(char)>1 and char not in duplicates:
        duplicates.append(char)

print(duplicates)