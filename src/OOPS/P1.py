class Student:
    def __init__(self, full_name):
        self.name = full_name
        print("Creating an Object")

s1 = Student("Abhijeet")
print(s1.name)