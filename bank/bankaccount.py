from pydantic import BaseModel, validator


class BankAccount(BaseModel):
    owner: str
    iban: str | None = None
    balance: int = 0
    transactions: list[dict] = []

    @validator('iban', always=True, pre=True)
    def set_iban(cls, v):
        return 'SK1234567890'


def test1():
    account = BankAccount(owner='janko hrasko')
    assert account.balance == 0


test1()
