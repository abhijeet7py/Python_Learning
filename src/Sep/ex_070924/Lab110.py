# Method Overloading
# Python does not support method overloading

class MathUtils(object): # is - a Object - single inheritance
#     Method Overloading - Not Supported
    def add(self,a,b):
        return a + b
    def add(self,a,b,c=0):
        return a + b + c

    def add(self,a,b,c=8,d=1):
        return a+b+c+d

math = MathUtils()
print(math.add(5,3))

