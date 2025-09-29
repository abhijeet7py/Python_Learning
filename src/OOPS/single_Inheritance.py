class Car:
    colour = "Black"
    @staticmethod
    def start():
        print("Car Started!")
    @staticmethod
    def stop():
        print("Car Stopped!")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Camery")

print(car1.name)
car1.start()