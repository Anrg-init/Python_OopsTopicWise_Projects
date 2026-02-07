## Account Mangment using DAC concept project

class BankAccount:
    def __init__(self, acc_no, owner, balance=0):
        self._acc_no = acc_no
        self._owner = owner
        self.__balance = balance


    @property
    def checkAc(self):
        return self._acc_no
    

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, name):
        if not name.strip():
            raise ValueError("name cant be empty")
        self._owner = name

    
    @property
    def checkbalance(self):
        return self.__balance
    
    def withdrawn(self, amount):
        if amount > self.__balance:
            raise ValueError("not enough balance")
        self.__balance = self.__balance - amount

    def deposit(self, amount):
        if amount<0:
            raise ValueError("enter valid amount")
        self.__balance = self.__balance + amount


    def Acc_info(self):
        return print(f"{self._owner} - {self._acc_no} - {self.__balance}")



Bank1 = BankAccount(12131, "anurag")
print(Bank1.checkAc)
print(Bank1.owner)
print(Bank1.checkbalance)
Bank1.owner = "jaskldfas"
Bank1.deposit(12332)


Bank1 = BankAccount(12131, "anurag")
print(Bank1.checkAc)
print(Bank1.owner)
print(Bank1.checkbalance)
Bank1.owner = "jaskldfas"
print(Bank1.owner)

Bank1.deposit(124124)
print(Bank1.checkbalance)
Bank1.Acc_info()
    