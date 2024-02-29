from pydantic import BaseModel


class BankAccount(BaseModel):
    balance: int = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount: int):
        if type(amount) is not int:
            raise TypeError('Amount is not an integer.')
        if amount <= 0:
            raise ValueError("Invalid amount.")

        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance - amount <= 0:
            raise ValueError('Not enough money.')

        self.balance -= amount
