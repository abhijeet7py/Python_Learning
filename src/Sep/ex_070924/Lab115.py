from abc import ABC, abstractmethod

class Excelreader(ABC):
    @abstractmethod
    def readfromexcel(self):
        pass

class Browser(Excelreader):
    @abstractmethod
    def startBrowser(self):
        pass
    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):
    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readfromexcel(self):
        print("Readfromexcel is ready")

    def runTC1(self):
        self.startBrowser()
        self.readfromexcel()
        self.stopBrowser()

TC = TC1()
TC.runTC1()