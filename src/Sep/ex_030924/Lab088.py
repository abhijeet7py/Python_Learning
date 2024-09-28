a = 10

class Person:

    b = 11 # Instance variable -> Belogs to the class
    c = 12 # Instance variable -> Belogs to the class

    def print_info(self):
        global a
        a = "Hello"
        print(a)
        print(self.b)
        print(self.c)


obj_ref = Person()
obj_ref.print_info()
print(a)
