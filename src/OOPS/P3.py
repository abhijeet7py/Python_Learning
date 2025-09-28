class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("Your balance is:",self.get_bal())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount, "Was Credited")
        print("Your balance is:",self.get_bal())

    def get_bal(self):
        return self.balance

acc1 = Account(10000,78459)
acc1.debit(500)
acc1.credit(45000)