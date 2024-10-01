class Bank:
    def __init__(self,account_no,balance):
        self.balance = balance
        self.__account_no = account_no

    def deposite(self,amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def check_Acc_no(self,is_auth):
        if is_auth == True:
            print(self.__account_no)

        else:
            print("Not allowed")

    def __internal_method(self):
        print("This is a Private method")
        print(self.__account_no)
        self.check_Acc_no()

hdfc = Bank(1245367809,400)
hdfc.deposite(500)
hdfc.check_balance()
hdfc.check_Acc_no(True)
hdfc.deposite(200)
hdfc.check_balance()
hdfc.check_Acc_no(False)

# hdfc.__internal_method()