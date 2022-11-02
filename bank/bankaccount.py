from pydantic import BaseModel, validator


class BankAccount(BaseModel):
    owner: str
    iban: str | None = None
    balance: int = 0
    transactions: list[dict] = []

    def deposit(self, amount: int):
        # is amount integer?
        if type(amount) != int:
            raise TypeError('Amount should be of type integer.')

        # is amount positive integer?
        if amount < 0:
            raise ValueError("Amount should be positive integer.")

        # make deposit
        self.balance += amount

    @validator("iban", always=True, pre=True)
    def set_iban(cls, v):
        return "SK1234567890"