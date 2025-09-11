# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.

# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    def book(abhi,fro,to):
        print(f"The Ticket is booked in train No:{abhi.trainNo} from {fro} to {to}")

    def trainStatus(self):
        print(f"Train No: {self.trainNo} is running on time.")
    def getFare(self,fro,to):
        print(f"Ticket fare in trainNo: {self.trainNo} from {fro} to {to} is: {randint(120,900)}")

t = Train("45215")
t.book("Pune", "Kolhapur")
t.trainStatus()
t.getFare("Pune","Kolhapur")