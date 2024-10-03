class ExcelReader:
    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MySQLDBConnection:
    @staticmethod
    def readMySQL():
        print("Reading My SQL")


class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()
        MySQLDBConnection.readMySQL()

tc = TC1()
tc.runTC()