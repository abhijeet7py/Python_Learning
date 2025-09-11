# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n = n

    @staticmethod
    def greet():
        print("Hello! Good Morning")
    def square(self):
        print(f"The Square is: {self.n*self.n}")
    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The Square Root is: {self.n ** 0.5}")

Calculator.greet()
user = int(input("Enter the Number: "))
calc = Calculator(user)
calc.cube()
calc.squareRoot()
calc.square()