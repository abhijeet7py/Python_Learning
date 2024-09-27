# Class and Object Assignment
#
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions
class Employee:
    # Constructor to initialize the employee's details
    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    # Method to simulate walking
    def walk(self):
        print(f"{self.name} is walking.")

    # Method to simulate talking
    def talk(self):
        print(f"{self.name} is talking.")

    # Method to print employee details
    def printdetails(self):
        print(f"Employee ID: {self.eid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
        print("-" * 20)


# Function to get employee details from the user
def get_employee_info():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    eid = input("Enter employee ID: ")
    return Employee(name, age, phone, address, eid)


# Getting information for Employee 1 (E1) and Employee 2 (E2)
print("Enter details for Employee 1 (E1):")
e1 = get_employee_info()

print("\nEnter details for Employee 2 (E2):")
e2 = get_employee_info()

# Printing details for both employees
print("\nDetails of Employee 1:")
e1.printdetails()

print("Details of Employee 2:")
e2.printdetails()

# Example of calling walk and talk methods
e1.walk()
e1.talk()

e2.walk()
e2.talk()


