class Parent():
    gold = "2 KG"

    def BHK2(self):
        print("2BHK")


class Child(Parent):
    diamond = "Diamond"

    def BHK3(self):
        print("3 BHK")


child_obj = Child()
child_obj.BHK3()
child_obj.BHK2()
print(child_obj.gold)
print(child_obj.diamond)

parent_obj = Parent()
parent_obj.BHK2()
print(parent_obj.gold)
parent_obj.BHK3()   # AttributeError: 'Parent' object has no attribute 'BHK3'. Did you mean: 'BHK2'?
# print(parent_obj.diamond)