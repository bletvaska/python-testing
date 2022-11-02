from bank.bankaccount import BankAccount


def test1():
    account = BankAccount(owner="janko hrasko")
    assert account.balance == 0, "Balance should be 0 when account was created."


# ked vlozim na prazdny ucet 100, tak zostatok bude 100
def test2():
    account = BankAccount(owner="janko hrasko")
    account.credit(100)
    assert account.balance != 100, "Balance should be 100."
