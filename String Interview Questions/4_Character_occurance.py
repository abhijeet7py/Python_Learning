s = "Automation"

result = {}

# Using for loop
for ch in s:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] = 1

print(result)

# Using get() method

counts = {}

for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

print(counts)

# Handle Spaces and Upper cases also

words = "Automation is gOod"
words = words.lower()

results = {}

for ch in words:
    if ch != " ": #Skips the Spaces
        results[ch] = results.get(ch, 0) + 1

print(results)
