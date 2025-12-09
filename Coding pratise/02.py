# Take 2 lists as input and give expected output

lis1 = ["My", "name"]
lis2 = ["is", "Abhijeet"]

# Exp = My name is Abhijeet

lis3 = lis1 + lis2
print(lis3)
lis1.extend(lis2)
print(lis1)

print(" ".join(lis1))
print(" ".join(lis3))