# Write a python program to count thr number
# of times a class is called

#1 - Using class Variable:

class Myclass:
    # class variable
    count = 0
    # defining constructor
    def __init__(self):
        Myclass.count += 1

# Creating object
a = Myclass()
b = Myclass()
c = Myclass()

print("Class called: ",Myclass.count," times")

# 2- Using globle variable

# define a global variable

count1 = 0

class A:
    def __init__(self):
        global count1 # tell python to use global variable
        count1 += 1

for i in range(1,5):
    a1 = A()

print("Class called: ",count1," times")
