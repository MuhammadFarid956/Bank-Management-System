# from accounts import Account
# from system_operations import Bank
#
# def main():
#     my_bank = Bank()
#
#     while True:
#         print("\n===== Welcome to Python Bank =====")
#         print("1. Create New Account")
#         print("2. Access Existing Account")
#         print("3. Close an Account")
#         print("4. Exit")
#
#         try:
#             choice = int(input("Enter your choice (1-4): "))
#
#             if choice == 1:
#                 my_bank.create_account()
#             elif choice == 2:
#                 my_bank.perform_transaction()
#             elif choice == 3:
#                 my_bank.close_account()
#             elif choice == 4:
#                 print("Thank you for using Python Bank. Godbye!")
#             else:
#                 print("Invalid choice. Please select a valid option.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#
# if __name__ == "__main__":
#     main()