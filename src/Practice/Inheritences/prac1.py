class Person:
    def show_info(self):
        print("I am a Person")

class Student(Person):
    def study(self):
        print("I am Studying")

x = Student()
x.show_info()
x.study()