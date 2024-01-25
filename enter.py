from bankaccount import *

Dave = BankAccount("Dave", 3000)
Sarae = BankAccount("Sarae", 3100)

Dave.getBalance()
Sarae.getBalance()

Sarae.deposit(100000)
Dave.withdraw(2000)
Dave.transfer(100, Sarae)
Sarae.transfer(100, Dave)

Jim = InterestRewardAcct("Jim", 1000)  
Jim.getBalance()  
Jim.deposit(100)
Jim.transfer(100, Dave)  

zetto = SavingsAcct(100000, "zetto")
zetto.getBalance()  # Corrected by adding parentheses
zetto.transfer(93800, Dave)
zetto.getBalance()
chips = SavingsAcct(1,"chips")
chips.getBalance()
chips.transfer(1,zetto)
chips.getBalance()
zetto.transfer(10000,chips)
Dave.transfer(10000,chips)
chips.getBalance()