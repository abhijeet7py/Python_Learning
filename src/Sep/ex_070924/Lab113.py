from abc import ABC , abstractmethod

class PyATB(ABC):
    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class abhi(PyATB):
    def payfee(self):
        print("Paid")


abhijeet = abhi()
abhijeet.enrolled()