class Employee:
    a = 1
    def __init__(self):
        print("Constructor of employee")
    def info(self):
        print("Information about employee")

class Manager(Employee):
    b = 2
    def __init__(self):
        print("constructor of Manager")

class Programmer(Manager):
    c = 3
    # def __init__(self):
    #     # super().__init__()
    #     print("Constrictor of Programmer")
    def info(self):
        super().info()
    

a = Programmer()
a.info()

