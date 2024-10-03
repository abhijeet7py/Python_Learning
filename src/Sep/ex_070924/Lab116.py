# Static Methods
# A static method is a method that belongs to a
# class rather than a instance of a class

class O:
    @staticmethod
    def sum(a,b):
        return a + b

class Mathoperations(O):
    def div(self,a,b):
        return a / b
    def mul(self,a,b):
        return a * b

    @staticmethod
    def sum(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b


# Non static in nature --> Object creation is Mandatory
obj_ref = Mathoperations()
output=obj_ref.div(4,5)
output2=obj_ref.mul(4,5)
print(output)
print(output2)

# Static methods can be called directly without the object

print(Mathoperations.sum(44,88))
print(Mathoperations.sub(4,5))
print(O.sum(5,8))
