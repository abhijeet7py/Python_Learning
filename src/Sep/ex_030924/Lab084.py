# Take input and create a class in python

class Person:

    def __init__(self):
        self.name = input("Enter the name: ")
        self.age = int(input("Enter the age: "))
        self.phone = int(input("Enter the phone no: "))

    def display_info(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")
        print(f"phone is {self.phone}")

# Create an object
person1 = Person()

# Call the dispaly function
person1.display_info()