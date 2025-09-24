class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "TCS"
#     def show(self):
#         print(f"The name is {self.name} and salary is {self.salary}")
#
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good at {self.language} language")

class Programmer(Employee):
    company = "Infi"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good at {self.language} language")

a = Employee()
b = Programmer()

print(a.company,b.company)