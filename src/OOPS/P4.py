from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass   # Only declaration, no implementation

    @abstractmethod
    def stop(self):
        pass

# Concrete class
class Car(Vehicle):

    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

# Trying to create object of Vehicle will give error
# v = Vehicle()  ❌ Not allowed

c = Car()
c.start()
c.stop()
