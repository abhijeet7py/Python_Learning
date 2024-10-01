# Multiple inheritance
class Father:
    key = "ABC"
    __Password = "Private"

    def __show_password(self):
        print(self.__Password)

    def father_money(self):
        return 500

    def home(self):
        return "This is from Father"

    def show_everything(self):
        return self.__show_password()

class Mother:
    def mother_money(self):
        return 200

    def home(self):
        return "This is from Mother"

class Son(Mother,Father): # MRO --> Method resolution Order
    pass

class Son2(Father,Mother):
    pass

s = Son()
s2 = Son2()
print(s.mother_money())
print(s.father_money())
print(s.home())
print(s2.home())

print(s.key)
s.show_everything()
