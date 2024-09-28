# user defined
# 1. they cant return --> no return
# 2. They cn return something
# They have parameters
# They dont have parameters/ arguments

# 1. they cant return --> no retun
# No retun type and no parameter / Argument

def greet():
    print("Hello world")

result = greet()
print(result)

# 2. Return type with argument
def greet_by_name(name):
    print("Hello,", name)

greet_by_name("Abhijeet")

# 3. No rturn type with default argument

def say_hello_default_arg(name="Abhi"):
    print("Hello,", name)

say_hello_default_arg("Abhijeet")
say_hello_default_arg()
say_hello_default_arg(name = "Pramod") # positional argument

def multiple_args(name1, name2, name3):
    print("Multiple Arguments,", name1, name2, name3)

multiple_args("ram", "yund",  "prvk")

# 4. Argument + return type

def sum_of_two_number(num1, num2):
    return num1 + num2

result = sum_of_two_number(1112, 2456)
print(result)
