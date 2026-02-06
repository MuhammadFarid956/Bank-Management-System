from bank_accounts import *

Udin = BankAccount(1000, "Udinn")
Asep = BankAccount(2000, "Asep")

Udin.getBalance()
Asep.getBalance()   

Udin.deposit(500)

Udin.withdraw(500)

Udin.transfer(50, Asep)

Ahmad = InterestRewardAcct(3000, "Ahmad")
Ahmad.deposit(1000)
Ahmad.getBalance()
Ahmad.transfer(500, Asep)

Owi = SavingsAcct(1500, "Owi")
Owi.getBalance()
Owi.deposit(1000)
Owi.withdraw(200)
Owi.transfer(1000, Asep)
