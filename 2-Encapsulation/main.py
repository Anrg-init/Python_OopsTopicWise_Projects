class BankAccount:
    bank_name = "UCO Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self._account_type = "Saving"
        self.__balance = balance

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Don't have sufficient balance"

    def show_account(self):
        return f"{self.bank_name} | {self.owner} | {self._account_type} | Balance: {self.__balance}"


print("Welcome to the ATM\n")
owner = input("Enter owner name: ")
balance = int(input("Enter your balance: "))
acc1 = BankAccount(owner, balance)


while True:
    print("\nChoose your service:")
    print("1 : Check Balance")
    print("2 : Withdraw")
    print("3 : Deposit")
    print("4 : Show Account")
    print("5 : Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", acc1.check_balance())

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        print("Balance:", acc1.withdraw(amount))

    elif choice == 3:
        amount = int(input("Enter amount to deposit: "))
        print("Balance:", acc1.deposit(amount))

    elif choice == 4:
        print(acc1.show_account())

    elif choice == 5:
        print("Thanks for using our ATM")
        break

    else:
        print("Invalid choice")
