# self refers to the instance of the class. It is automatically passed with a function call
# from an object.

class Employee:
    language = "Python"
    salary = 750000

    # here self is harry
    # equivalent to Employee.getSalary(harry)
    # def getinfo():
    #     print(f"The language is {self.language} and salary is {self.salary}")
    def getinfo(self):
        print(f"The language is {self.language} and salery is {self.salary}")

        #Sometimes we need a function that does not use the self-parameter. We can define a
        # static method like this:

    @staticmethod
    def greet():
        print("Good Morning!")
abhi = Employee()
abhi.language = "Javascript"
abhi.greet()
abhi.getinfo()
