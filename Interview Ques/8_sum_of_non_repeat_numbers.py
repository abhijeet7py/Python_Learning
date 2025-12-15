nums = [2, 3, 5, 3, 2, 6, 7]

freq = {}

for num in nums: # iterate over each element from list
    if num in freq: # check if num is already present in freq.
        freq[num] += 1 # if its present add value by 1
    else:
        freq[num] = 1 # else set the value to 1

print("Occurance: ", freq) # print the occurances

sum = 0 # declare a sum variable to calculate the sum with 0

for num in freq: # iterarate over each element from freq
    if freq[num] == 1: # checks if value of num = 1
        sum += num # if it is 1 add the

print("Sum: ", sum)