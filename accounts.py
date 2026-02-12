from system_operations import Account, System

class Accounts:
    def __init__(self):
        self.accounts = []
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

    def create_acc(self, acc_name, acc_balance):
        new_acc_num = System.gen_acc_num()
        new_acc = Account(new_acc_num, acc_name, acc_balance)
        self.accounts.append(new_acc)
        System.save_data()
        return new_acc

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance : ${self.balance}")
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
