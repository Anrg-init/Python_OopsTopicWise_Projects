#this project is done by using data access control concepts like getter setter and property defination

class ewallet:
    def __init__(self, userid, username, balance=0):
        self._userid = userid
        self._username = username
        self.__balance = balance

    
    @property
    def userid(self):
        return self._userid
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,name):
        if not name.strip():
            return ValueError("enter valid name")
        else:
            self._username = name

    
    @property
    def balance(self):
        return self.__balance


    def add_money(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount


    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Invalid payment amount")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount


    @property
    def wallet_summary(self):
        return f"{self.username} | Balance: ₹{self.__balance}"
  




wallet = ewallet(1001, "Anurag", 500)

print(wallet.userid)        
print(wallet.username)
print(wallet.balance)

wallet.add_money(1000)
wallet.pay(300)

wallet.username = "Rahul"
print(wallet.wallet_summary)
