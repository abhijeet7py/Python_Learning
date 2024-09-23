# @staticmethod
# @classmethod
# @property
#
# # These we will use in the oops

def decorator_1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator_2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator_1
@decorator_2
def say_hello():
    print("Hello")

say_hello()