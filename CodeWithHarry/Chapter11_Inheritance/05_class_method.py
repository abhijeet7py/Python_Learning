class Employee:
    a = 10
    @classmethod
    def show(cls):
        print(f"The class value is {cls.a}")


e = Employee()
# e.a = 100
e.show()