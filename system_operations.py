from accounts import  Account

class Bank:
    def __init__(self):
        self.accounts = {} #Dictionary

    def create_account(self):
        name = input("Enter account holder's name : ")
        try:
            initial_deposit = float(input("Enter initial deposit amount: $ "))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative")
                return
            new_account = Account(name, initial_deposit)
            self.accounts[new_account.account_number] = new_account
        except ValueError:
            print("Invalid input for deposit. Please enter a number")

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def close_account(self):
        account_number = input("Enter account number to close : ")
        account = self.find_account(account_number)
        if account:
            print(f"closing account for {account.name}")
            del self.accounts[account_number]
            print(f"account closed successfully.")
        else:
            print("Account not found.")

    def perform_transaction(self):
        account_number = input("Enter your account number : ")
        account = self.find_account(account_number)

        if not account:
            print("Account not found")
            return

        while True:
            print("\nTransaction Menu:")
            print("1. Deposit : ")
            print("2. Withdraw : ")
            print("3. Check Balance : ")
            print("4. View Account Details : ")
            print("5. Exit Transaction Menu : ")

            try:
                choice = int(input("Enter your choice (1-5) : "))

                if choice == 1:
                    amount = float(input("Enter amount to deposit : $"))
                    account.deposit(amount)
                elif choice == 2:
                    amount = float(input("Enter amount to withdraw : $"))
                    account.withdraw(amount)
                elif choice == 3:
                    account.check_balance()
                elif choice == 4:
                    account.display_details()
                elif choice == 5:
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input.Please enter a number")