class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    def showDetails(self):
        print("Role = ", self.role)
        print("Department = ",self.dept)
        print("Salary = ", self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","60000")
# e1 = Employee("Accontant","Fianance","45000")
engg1 = Engineer("Abhijeet",26)
engg1.showDetails()