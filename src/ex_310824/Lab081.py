class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour
    def talk(self): #NRNA # self - self will be first argument in every behaviour
        print("I can Talk")

    def sleep(self,name): # Arg with no return
        print("I am a Method")
        print("Sleep", name)

    def sleep2(self, name): # Arg with return
        print("I am a Method")
        return None

    def walk(self):
        print("I am Walking")

    def walk_return(self): # No arg with return
        return "I am Walking"


# Create an object of the class
# ObjectRef = ClassName() -> Object

tushar = Person()
tushar.name = "Tushar"
print(tushar.name)
tushar.talk()


rajyalakshmi = Person()
rajyalakshmi.name = "rajyalakshmi"
print(rajyalakshmi.name)
rajyalakshmi.talk() 