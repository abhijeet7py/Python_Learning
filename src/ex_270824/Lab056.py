# Function scope
global_b = 12 # almost work like global variable

# Local variable have more preference over the global variables
def my_function():
    a = 10 # Local variable, within the function
    print(a)
    print(global_b)

def f1():
    print(global_b)

# print(a)
my_function()
print(global_b)
