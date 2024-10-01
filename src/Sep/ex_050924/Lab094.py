a = 10 # Global variable

class Myclass:
    # Public variable (instance)
    public_var = "I am Public"
    __balance = 1000  # Private variable

    # Private variable
    __private_var = "I am Private"
    __password = 1234

    # Protected variable
    _protected_var = "I am Protected"
    b = 10 # Public variable
    _c = 20 # Protected variable
    __d = 30 # Private variable

    collage = "D Y Patil"
    __bank_balance = 10000



object = Myclass()

print(object.public_var)
print(object._protected_var)
print(object.__private_var)
print(object.__password)