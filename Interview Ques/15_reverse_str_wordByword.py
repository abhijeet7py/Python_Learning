s = "Automation Testing is good"

# 1. using Split and slicing:

words = s.split() # Split divides the string where there is space
                  # so words = ["Automation","Testing","is","good"]

reverse = words[::-1]  # reverse the words

result = " ".join(reverse) # join combines list elements into string using space as a separator
print(result)

# 2. Using for loop
words = s.split()  # using split will convert string into list
rev = ""           # initialize empty string for storing reversed string
for i in range(len(words)-1, -1, -1):  # len(words) - 1 = last index
                                       # -1 = stop before index -1, -1 = move backward
    rev += words[i] + " " # appends word in reverse order

print(rev)