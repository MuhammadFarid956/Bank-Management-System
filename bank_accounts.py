class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit Completed.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Sorry, account '{self.name}'  only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")
    
    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nBeginning Transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\Transfer Complete!\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer Interrupted: {error}")

class InterestRewardAcct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete! (with 5% interest reward)")
        self.getBalance()

class SavingsAcct(BankAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f"\nWithdraw Complete! (including ${self.fee} fee)")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")


             
      