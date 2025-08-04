s1 = {21,112,221.34,"Abhi","pramod","World",True}
s2 = {12,22,21}

# s1.add(22)
# s1.update([22])
print(s1)
# s1.remove(25) # Raise key error when item is not found in set
s1.discard(45) # Does not raise error when item is not found in set
s1.pop() # Removes an random item from the set
# s1.clear() # This will empty the set
print(s1)

print(s1.union(s2))
print(s1.intersection(s2))