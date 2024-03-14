class BankAccount:
    int_rate = 0.01

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        self.balance += self.balance * self.int_rate


class SavingsAccount(BankAccount):
    def __init__(self, int_rate=0.01, balance=0):
        super().__init__(int_rate, balance)

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        super().withdraw(amount)

    def display_account_info(self):
        super().display_account_info()

    @staticmethod
    def check_balance(balance, savings):
        if balance > 0:
            return True
        if savings > 0:
            return True
        else:
            return False


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.savings = SavingsAccount(int_rate=0.02, balance=0)

    # Account Methods:
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def calc_interest_yield(self):
        self.account.yield_interest()

    def transfer_money(self, amount, other_user):
        if isinstance(other_user, User):
            if self.account.balance >= amount:
                self.account.withdraw(amount)
                other_user.account.deposit(amount)
            else:
                print("Insufficient funds.")

    # Savings Methods:
    def make_savings_deposit(self, amount):
        self.savings.deposit(amount)

    def make_savings_withdrawal(self, amount):
        self.savings.withdraw(amount)

    def calc_savings_interest_yield(self):
        self.savings.yield_interest()

    def display_user_balance(self):
        print("Account Information:")
        self.account.display_account_info()
        print("Savings Account Information:")
        self.savings.display_account_info()


# User 1:
user_1 = User("Jason", "jason@codingdojo.com")

user_1.make_deposit(250)
user_1.make_withdrawal(100)
user_1.calc_interest_yield()

user_1.make_savings_deposit(500)
user_1.make_savings_withdrawal(100)
user_1.calc_savings_interest_yield()

user_1.display_user_balance()


# User 2:
user_2 = User("Monica", "monica@gmail.com")

user_2.make_deposit(250)
user_2.transfer_money(100, user_1)
user_2.calc_interest_yield()
user_2.display_user_balance()
user_1.display_user_balance()
