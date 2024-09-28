# Web Autoamation -- Selenium
# Page - you are going to automate

class VWOloginpage:

    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "abhijeet@gmail.com" and self.password == "Pass123":
            print("Allowed to login")
        else:
            print("Not allowed")

email = input("Enter your email: \n")
password = input("Enter your password: \n")

vwo_obj = VWOloginpage(email,password)
vwo_obj.login_confirm()