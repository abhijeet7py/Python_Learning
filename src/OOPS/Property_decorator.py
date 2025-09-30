class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
    # def calPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    # There is better way Using @Property method
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

s1 = Student(78,88,74)
print(s1.percentage)
s1.phy = 49
# s1.calPercentage()
print(s1.percentage)

