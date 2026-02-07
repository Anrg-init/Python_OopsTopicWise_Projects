#Transport oops project uisng concepts of inheritance

class Transport:
    def __init__(self,  brand,fuel):
        self.brand = brand
        self.fuel = fuel

    def start(self):
        print(f"{self.brand} transport started")

    def fule_type(self):
        print(f"{self.fuel} is fule type of {self.brand}")


class Car(Transport):
    def __init__(self, brand, fuel, model):
        super().__init__(brand, fuel)
        self.model = model

    def start(self):
        print(f"{self.model} of {self.model} started ")

    def detail(self):
        print(f"model : {self.model}")

class Bike(Transport):
    def __init__(self,brand,fuel,mlg):
        super().__init__(brand,fuel)
        self.mlg = mlg

    def start(self):
        print(f"{self.brand} started")

    def detail(self):
        print(f" mileage : {self.mlg}")



car1 = Car('tata', 12, 'rangerover')
car1.start()
car1.detail()
car1.fule_type()