# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod

class Fathar(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Son(Fathar):
    pass
    # def loan(self):
    #     print("Paid")

s = Son("Abhi")
s.loan()