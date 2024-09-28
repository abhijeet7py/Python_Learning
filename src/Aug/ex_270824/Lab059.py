# Understanding decoratrs in python

# Decorators in python are a way to modify the behavior of a function or class without changing its source code
# They are a powerful tool that allows you to wrap another function and extend its functionality,
# while keeping the original function's code unchanged.

def my_decorator(func):
    # Two parts
    # wrapper & call
    def wrapper():
        print("1.Before the function is called.")
        print("2.Add Helmet,Dashcam, gloves")
        func()
        print("3.After the function is called.")
        print("4.Secure driving")
    return wrapper()

# defination
@my_decorator
def drive_bike():
    print("I am driving")

# Call to the function
# drive_bike()