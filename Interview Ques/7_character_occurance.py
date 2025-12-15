str = "automation"

result = {}

# 1. using dictionary approach

for ch in str: # for loop iterate over the string
    if ch in result: # if statement will check if character is available in result if yes it will increment the value
        result[ch] += 1
    else: # if not it will be added 1
        result[ch] = 1

print(result)

# 2. without dictionary

occ = []

for ch in str: # iterate over each character
    if ch not in occ: # check if character is already processed
        count = 0 # initialize the counter
        for c in str: # compares current char. ch to every char. in c of str.
            if c == ch:
                count += 1 # Increment in count when match is found
        print(ch, ":", count) # print the result
        occ.append(ch) # add character to occ. so it is not counted again

print(occ)





