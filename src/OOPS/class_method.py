class Person:
    name = "Annonymous"

    def changeName(self,name):
        self.name = name
        Person.name = name #One of way to change the class attributes
        self.__class__.name = name # Another way of to change class attributes

    # Using Class method decorator
    @classmethod
    def change(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Abhijeet")
print(p1.name)
print(Person.name)

p2 = Person()
p2.change("Abhi")
print(p2.name)