#another example using advanced conepts like mro super() and other inheritance advanced part

class Vehicle:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started")

    def info(self):
        print("general vehicle")


class Fuelvehicle(Vehicle):

    def start(self):
        print(f"{self.brand} fuel vehicle started")

    def info(self):
        print(f"fuel vehicle")

class Electricvehicle(Vehicle):
    
    def start(self):
        print(f"{self.brand} electric vehicle started")

    def info(self):
        print("electric vehicle")



class Autonomousvehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} autonous veh started")

    def info(self):
        print("it's a autonous vehicle")



class hybridcar(Fuelvehicle, Electricvehicle, Autonomousvehicle):

    def start(self):
        print(f"{self.brand} hydbrid car started")
        super().start()

    def info(self):
        print("hybridcar started ")


    
obj1 = hybridcar("tata")
obj1.start()
