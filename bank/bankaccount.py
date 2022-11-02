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
    assert account.balance == 0, 'Balance should be 0 when account was created.'


"""
ked vlozim na prazdny ucet 100, tak zostatok bude 100
"""
def test2():
    account = BankAccount(owner='janko hrasko')
    account.credit(100)
    assert account.balance == 100, 'Balance should be 100.'

test1()
test2()
