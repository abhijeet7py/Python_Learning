#Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p1 = Programmer("Abhijeet",1234567,213311)
print(p1.name,p1.salary,p1.pin,p1.company)
