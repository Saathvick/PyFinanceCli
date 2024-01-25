class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"\n{self.name} has this much balance {self.balance}\n")

    def getBalance(self):
        print(f"\nAccount {self.name} balance {self.balance}\n")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete")
        self.getBalance()

    def viabletransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viabletransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*************\n\n Beginning Transfer..')
            self.viabletransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer complete\n\n ***********')
        except BalanceException as error:
            print(f'\nTransfer interrupted..{error} ')


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete with interest")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialamount, accName):
        super().__init__(accName, initialamount)  
        self.fee = 5

    def withdrawal(self, amount):
        try:
            self.viabletransaction(amount + self.fee) 
            self.balance = self.balance - (amount + self.fee)
            print("Withdrawal completed")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
