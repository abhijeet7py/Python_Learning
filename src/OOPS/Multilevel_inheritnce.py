class Car:
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car Stopped!")

class Toyota(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Petrol")
car1.start()