import csv
import os
import random
from accounts import Accounts

FILENAME = "accounts_data.csv"

class Utility:
    def __init__(self):
        self.accounts = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(FILENAME):
            return

        try:
            with open(FILENAME, 'r') as file:
                reader = csv.reader(file)
                self.accounts = [Accounts(*row) for row in reader if row]
        except FileNotFoundError:
            print("File not found.")

    def save_data(self):
        try:
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(acc.to_list() for acc in self.accounts)
        except FileNotFoundError:
            print("File not found. Can't save data.")

    @staticmethod
    def gen_acc_num():
        return ''.join(str(random.randint(0,9) for _ in range(10)))

# class Bank:
#     def __init__(self):
#         self.accounts = {} #Dictionary
#
#     def create_account(self):
#         name = input("Enter account holder's name : ")
#         try:
#             initial_deposit = float(input("Enter initial deposit amount: $ "))
#             if initial_deposit < 0:
#                 print("Initial deposit cannot be negative")
#                 return
#             new_account = Account(name, initial_deposit)
#             self.accounts[new_account.account_number] = new_account
#         except ValueError:
#             print("Invalid input for deposit. Please enter a number")
#
#     def find_account(self, account_number):
#         return self.accounts.get(account_number)
#
#     def close_account(self):
#         account_number = input("Enter account number to close : ")
#         account = self.find_account(account_number)
#         if account:
#             print(f"closing account for {account.name}")
#             del self.accounts[account_number]
#             print(f"account closed successfully.")
#         else:
#             print("Account not found.")
