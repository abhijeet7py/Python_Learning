class Employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"The name of Emploee is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printLanguage(self):
        print(f"Your Language is {self.language}")

class Programmer(Employee,coder):
    company = "TCS"
    def showInfo(self):
        print(f"The name is {self.name} and language is {self.language}")


a = Programmer()

a.showInfo()
a.show()
a.printLanguage()
print(Programmer.mro())

