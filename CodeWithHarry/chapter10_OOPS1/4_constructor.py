class Employee:
    def __init__(self,name,language,salary):
        print("I am creating an Object")
        self.name = name
        self.language = language
        self.salary = salary

    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The Language is {self.language} and Salary is {self.salary}")
    @staticmethod
    def greet(self):
        print("Good Morning!")

abhi = Employee("Abhijeet","Java",1200000)
print(abhi.salary,abhi.name,abhi.language)