# Conditions and loops

# Write a program to take a user age and let him know if he can go to club.
# 21

# Logic building
# 1. User input -- Data type -- int
# o/p -> string -> user if he can go or no

# Rough logic
# age > 21 --? print can go
# age < 21 ==> print cant go

age = int(input("Enter you age: "))

if age >= 21:
    print("You can go to club")
else:
    print("You can't go to club")