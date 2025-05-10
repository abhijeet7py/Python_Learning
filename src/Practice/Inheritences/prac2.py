class Employee:
    def __init__(self,name, salary):
        self.name =  name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name, salary, department):
        super().__init__(name,salary)
        self.department = department

    def show(self):
        print(f"Name: {self.name}, salary = {self.salary},Department:{self.department}")

e1 = Manager("ahjfb",231123,"HR")
e1.show()
