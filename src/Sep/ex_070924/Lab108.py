# Method Overriding
# says that, Child or subclass can have same name method as the parent or superclass

class Shape:

    def area(self):
        print("Print the area of the shape")


class Rectangle(Shape):
    def __init__(self,lenth,width):
        self.lenth = lenth
        self.width = width

    def area(self):
        return self.lenth * self.width

class Circle(Shape):
    def __init__(self,radious):
        self.radious = radious

    def area(self):
        return 3.14 * self.radious * self.radious


shape1 = Rectangle(3,5)
shape2 = Circle(10)
print(shape1.area())
print(shape2.area())
