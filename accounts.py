from operational import Utility

# FILENAME = "accounts.txt"

class Accounts:
    def __init__(self, account_name, initial_deposit):
        self.acc_num = Utility.gen_acc_num()
        self.acc_name = account_name
        self.acc_balance = initial_deposit
        self.accounts = []

    def to_list(self):
        return [self.acc_num, self.acc_name, self.acc_balance]

    def create_acc(self, new_acc_num):
        self.acc_num = new_acc_num
        new_acc = self.to_list()
        self.accounts.append(new_acc)
        Utility.save_data()
        return new_acc

    def deposit(self, amount):
        if amount > 0:
            self.acc_balance += amount
            print(f"Deposited ${amount}. New balance : ${self.acc_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance : ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient founds")

    def check_balance(self):
        print(f"Current balance for account {self.account_number}: ${self.balance} ")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder : {self.name}\nAccount Number : {self.account_number}\nBalance : {self.balance}")
        print("-" * 30)

    # def __init__(self, name, initial_deposit):
    #     self.name = name
    #     self.balance = initial_deposit
    #     self.account_number = self.generate_account_number()
    #     print(f"Account for {self.name} created successfully.")
    #     print(f"Your Number is: {self.account_number}")
    #
    # def generate_account_number(self):
    #     # Simple generate a 10-digit account number
    #     return ''.join([str(random.randint(0,9)) for _ in range(10)])
if __name__ == "__main__":
    user = Accounts
    user.create_acc('')
