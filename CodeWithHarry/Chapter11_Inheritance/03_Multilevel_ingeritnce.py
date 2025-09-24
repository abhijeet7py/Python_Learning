class Grandparent:
    def house(self):
        print("Grandparent: Owns a house")

class Parent(Grandparent):
    def car(self):
        print("Parent: Owns a car")

class Child(Parent):
    def bike(self):
        print("Child: Owns a bike")


a = Child()

a.bike()
a.car()
a.house()