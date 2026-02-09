# ===============================
# POLYMORPHISM PROJECT (ONE FILE)
# ===============================


# ---------- 1. Polymorphism: Same method name ----------
class BikeRide:
    def calculate_fare(self):
        print("Bike fare: ₹50")


class CarRide:
    def calculate_fare(self):
        print("Car fare: ₹120")


# ---------- 2. Duck Typing ----------
class CashPayment:
    def pay(self):
        print("Paid using Cash")


class UPIPayment:
    def pay(self):
        print("Paid using UPI")


def make_payment(payment):
    # Python only checks if pay() exists
    payment.pay()


# ---------- 3. Method Overriding Polymorphism ----------
class Ride:
    def start(self):
        print("Ride started")


class LuxuryRide(Ride):
    def start(self):
        print("Luxury ride started with AC")


# ---------- 4. Operator Polymorphism ----------
class Fare:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        # Defines what + means for Fare objects
        return Fare(self.amount + other.amount)

    def show(self):
        print("Total Fare: ₹", self.amount)


# ===============================
# RUN EVERYTHING
# ===============================

print("\n--- Polymorphism (Same Method Name) ---")
rides = [BikeRide(), CarRide()]
for r in rides:
    r.calculate_fare()


print("\n--- Duck Typing ---")
make_payment(CashPayment())
make_payment(UPIPayment())


print("\n--- Method Overriding ---")
r1 = Ride()
r2 = LuxuryRide()
r1.start()
r2.start()


print("\n--- Operator Polymorphism ---")
f1 = Fare(120)
f2 = Fare(80)
total = f1 + f2
total.show()
