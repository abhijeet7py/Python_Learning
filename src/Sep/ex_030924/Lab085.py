class Calc:

    def __init__(self):
        print("Default Constructor")

    def sum(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b


object_ref = Calc()

a = int(input("Enter first value: "))
b = int(input("Enter Second value: "))

output_sum = object_ref.sum(a,b)
output_sub = object_ref.sub(a,b)
output_mul = object_ref.mul(a,b)
output_div = object_ref.div(a,b)

print(output_sum, output_sub, output_mul, output_div)