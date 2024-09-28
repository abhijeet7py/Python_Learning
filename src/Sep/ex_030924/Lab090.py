class Person:
    # Class variables
    # Instance variables
    # name = "Amit" # hardcode value
    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name

amit = Person("Amit")
pramod = Person("Pramod")
print(amit.name)
print(pramod.name)

print("Who is walking with the object Pramod ->", pramod.walk())
