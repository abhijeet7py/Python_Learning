# Method Overriding - same name in the parent and child
# child always override the parent functions
# super means call my parent function

class GrandFathar:
    x = 10
    def home(self):
        print("Old home")

class Fathar(GrandFathar):
    a = 12
    def home(self):
        print("1 BHK")
        print(self.a)
        print(super().x)

class Son(Fathar):
    b = 15
    def home(self):
        super().home() # Fathar behaviour from super()
        print(super().a) # Fathar attributes from super()
        print("No House")
        print(self.b)

#         self = Me
#         super() = Parent, Superclass

abhi = Son()
abhi.home()
print(abhi.x)
