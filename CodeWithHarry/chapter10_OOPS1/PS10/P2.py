# Write a class “Calculator” capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The Square is: {self.n*self.n}")
    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The Square Root is: {self.n ** 0.5}")

user = int(input("Enter the Number: "))
calc = Calculator(user)
calc.cube()
calc.squareRoot()
calc.square()