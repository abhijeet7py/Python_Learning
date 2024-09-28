# Constructor
# Its a special function in class, __init__()
# It will be automatically called when you create an object

class Dog:
    name = None
    age = None


    def __init__(self,name,age):
        print("Called, Object is created")
        self.name = name
        self.age = age


    def sleep(self):
        print("Sleeping")
        print("Who is sleeping -> ", self.name,self.age)
        return None


dog1 = Dog("Chow", 4)
print(dog1.name)
dog1.sleep()

dog1.sleep()
# print(dog1.color)
print(id(dog1))

dog2 = Dog("mow", 20)
print(dog2.name)
dog2.sleep()
# print(dog2.color)
print(id(dog2))


# print(name)
