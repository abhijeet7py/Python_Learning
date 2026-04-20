s = "Automation testing is good"

# Reverse with Split and slice methods

s = s.split() # split() method converts string into list of words

rev = s[::-1] # Using slice reversing the words

rev = " ".join(rev)
print(rev)




revs = ""
# Reverse with split and for loop
for ch in range(len(s)-1 , -1, -1): #
    revs += s[ch] + " "

print(revs)
