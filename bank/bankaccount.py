from pydantic import BaseModel, validator


class BankAccount(BaseModel):
    owner: str
    iban: str | None = None
    balance: int = 0
    transactions: list[dict] = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Amount should be positive integer.')
        self.balance += amount

    @validator("iban", always=True, pre=True)
    def set_iban(cls, v):
        return "SK1234567890"
