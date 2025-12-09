# Combine 2 lists and convert it into a dictionary
# Expected: {a:1,b:2,c:3}

lis1 = ["a" , "b" , "c"]
lis2 = [1, 2, 3]

# 1. Zip method
dict1 = dict(zip(lis1,lis2))
print(dict1)

# 2. using dictionary comprehension

dict2 = {lis1[i]:lis2[i] for i in range(len(lis1))}
print(dict2)

# 3 Using for loops (Not recommended)

dict3 = {}
for key in lis1:
    for value in lis2:
        dict3[key] = value
        lis2.remove(value)
        break
print(dict3)



