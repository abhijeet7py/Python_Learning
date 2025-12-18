data = [10, 20.5, "python", True, 30, "40", None, 5]

total = 0

for item in data:
    if type(item) == int or type(item) == float:
        total += item
    elif type(item) == str and item.isdigit():
        total += int(item)

print("The total is", total)