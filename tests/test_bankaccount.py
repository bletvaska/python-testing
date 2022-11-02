import pytest

from bank.bankaccount import BankAccount


def test_when_account_was_created_then_balance_is_0():
    # arrange + act
    account = BankAccount(owner="janko hrasko")

    # assert
    assert account.balance == 0, "Balance should be 0 when account was created."


def test_when_100_is_added_to_empty_account_then_balance_should_be_100():
    # arrange
    account = BankAccount(owner="janko hrasko")

    # act
    account.deposit(100)

    # assert
    assert account.balance == 100, "Balance should be 100."


def test_when_deposit_to_account_with_nonzero_balance_then_final_balance_is_higher():
    # arrange
    old_balance = 50
    deposit = 80
    account = BankAccount(owner="janko hrasko", balance=old_balance)

    # act
    account.deposit(deposit)

    # assert
    assert (
        account.balance == old_balance + deposit
    ), f"Balance should be {old_balance + deposit}."


def test_when_negative_amount_is_deposited_then_valueerror_exception_should_be_thrown():
    # arrange
    amount = -100
    account = BankAccount(owner="sherlock holmes")

    # act + assert
    with pytest.raises(ValueError):
        account.deposit(amount)
