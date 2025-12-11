nums = [10, 252, 3, 99, 54]

# 1. using a simple loop
largest = nums[0]  #assumeing first element is largest

for num in nums:
    if num > largest:
        largest = num

print("Largest number: ",largest)

# 2. Using index iteration
largest = nums[0]

for i in range(1, len(nums)): # started index from 1 as 0 index is used in largest
    if nums[i] > largest:
        largest = nums[i]

print("Largest number: ",largest)
