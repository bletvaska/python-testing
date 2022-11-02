from bank.bankaccount import BankAccount


def test_when_account_was_created_then_balance_is_0():
    account = BankAccount(owner="janko hrasko")
    assert account.balance == 0, "Balance should be 0 when account was created."


def test_when_100_is_added_to_empty_account_then_balance_should_be_100():
    account = BankAccount(owner="janko hrasko")
    account.credit(100)
    assert account.balance == 100, "Balance should be 100."

def test_when_credit_is_deposited_to_account_with_nonzero_balance_then_final_balance_is_higher():
    old_balance = 50
    deposit = 80
    account = BankAccount(owner='janko hrasko', balance=old_balance)
    account.credit(deposit)
    assert account.balance == old_balance + deposit, f'Balance should be {old_balance + deposit}.'
