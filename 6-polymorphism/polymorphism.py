#contain all the concept of the polymorphism concept

class Email:
    def send(self):
        print("email send")

class whatsapp:
    def send(self):
        print("what's app send")

class sms:
    def send(self):
        print("sms send")

def notify(service):
    service.send()



#___________________________
class payment:
    def send(self):
        print('payment done')


class upi(payment):
    def send(self):
        print("payment using upi")

class card(payment):
    def send(self):
        print("payment using card")


#________________________

class bill:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self,other):
        return bill(self.amount + other.amount)
    
    def show(self):
        print(f"bill is : {self.amount}")       






# Duck typing + same method name
notify(sms())
notify(Email())


#mehod overriding
ob1 = card()
ob1.send()

ob2 = upi()
ob2.send()
    

#adding two objects
obj1 = bill(100)
obj2 = bill(200)
obj3 = bill(200)
total = obj1 + obj2 + obj3
total.show()