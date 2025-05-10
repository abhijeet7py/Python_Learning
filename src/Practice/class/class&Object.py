# class = class is like a blueprint or template to create the objects
# Object = A object is a real instance of the class

# A class has
# 1. attributes = variableas or data
# 2. methods = functions that what it do/ Behaviour

# Every Object:
# 1. has its attributes and functions defined by class
# 2. Can be created by call like a function

# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#
#     def show_info(self):
#         print(f"Brand: {self.brand} and color = {self.color}")
#
#
# my_car = Car("Toyota","red")
# my_car.show_info()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

