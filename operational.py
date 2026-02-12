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

