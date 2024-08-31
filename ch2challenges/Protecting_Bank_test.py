class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__initial_balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__initial_balance

    def deposit(self, amount):
        self.amount = amount
        if self.amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")
        else:
            self.__initial_balance += self.amount

    def withdraw(self, amount):
        self.amount = amount
        if self.amount <= 0:
            raise ValueError("Cannot withdraw zero or negative funds")
        elif self.amount > self.__initial_balance:
            raise ValueError("Insufficient funds")
        else:
            self.__initial_balance -= self.amount
