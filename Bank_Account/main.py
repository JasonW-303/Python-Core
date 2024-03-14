class BankAccount:
    int_rate = 0.01

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if BankAccount.check_balance(self.balance):
            self.balance = self.balance + (self.balance * self.int_rate)
        else:
            return

    @staticmethod
    def check_balance(balance):
        if balance > 0:
            return True
        else:
            return False


account_1 = BankAccount(BankAccount.int_rate, 0)

account_1.deposit(100)
account_1.deposit(100)
account_1.deposit(100)
account_1.withdraw(50)

account_1.yield_interest()

account_1.display_account_info()


account_2 = BankAccount(BankAccount.int_rate, 0)

account_2.deposit(100)
account_2.deposit(100)
account_2.withdraw(100)
account_2.withdraw(100)
account_2.withdraw(100)
account_2.withdraw(100)

account_2.yield_interest()

account_2.display_account_info()
