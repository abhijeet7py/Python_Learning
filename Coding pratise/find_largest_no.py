num = [12,123,1234,4521,3232,542,5]

large = num[0]

#Using simple loop

for i in num:
    if i > large:
        large = i

print("Large number: ",large)

# Using index iteration

largest = num[0]

for i in range(1, len(num)):
    if num[i] > largest:
        largest = num[i]

print("Large number: ",largest)


# If there are Strings and Negative numbers in list

nums = [123, "123", True, "abc", 321, -334]

larger = None

for i in nums:
    if isinstance(i, int):
        if larger is None or i > larger:
            larger = i

print("Large number: ",larger)


# When all are strings
numb = ["12", "123", "45", "abc", "-200", "67", "True"]

larg = None

for i in numb:
    try:
        val = int(i)
        if larg is None or val > larg:
            larg = val

    except:
        continue

print("Large number: ",larg)
