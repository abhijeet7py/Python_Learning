# Inheritance
class Father:
    key = "2BHk"

    def car(self):
        print("Father car --> Alto" , self.key)

class Son(Father):
    key2 = "3BHK"

    def truck(self):
        print("Son truck --> truck", self.key2)


father_obj = Father()
father_obj.car()
print(father_obj.key)
# father_obj.truck()

son_obj = Son()
son_obj.car()
# father_obj.truck()