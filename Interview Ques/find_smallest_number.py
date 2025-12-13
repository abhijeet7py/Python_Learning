nums = [110, 252, 312, 929, 514]

smallest = nums[0]

# 1. Using for loop
for num in nums:
    if num < smallest:
        smallest = num

print(f"The smallest number is: {smallest}")

# 2. Using index iteration
for i in range(1,len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]

print(f"The smallest number is: {smallest}")

# 3. Using while loop
smallest = nums[0]

i = 1

while i < len(nums):
    if nums[i] < smallest:
        smallest = nums[i]
    i += 1
print(f"The smallest number is: {smallest}")

