arr = [-10, 5, -20, -8, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and num > second_largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest number does not exist")
else:
    print("Second largest number:", second_largest)
