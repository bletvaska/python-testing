from pydantic import BaseModel, validator


class BankAccount(BaseModel):
    owner: str
    iban: str | None = None
    balance: int = 0
    transactions: list[dict] = []

    def credit(self, amount):
        self.balance += amount

    @validator("iban", always=True, pre=True)
    def set_iban(cls, v):
        return "SK1234567890"
