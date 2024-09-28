class Car:

    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with name ",self.name)
        print("Starting a car with make ",self.make)
        print("Starting a car with model ",self.model)


lambo = Car("Lambo","V12",2021)
lambo.start_engine()
xuv = Car("XUV","V6","2022")
xuv.start_engine()
