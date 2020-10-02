import random
import pytest

from bank import BankAccount


@pytest.fixture
def account():
    """
    Creates account with 0 balance.
    :return:
    """
    account = BankAccount()
    return account


@pytest.fixture
def account_with_random_balance():
    account = BankAccount()
    account.credit(random.randint(100, 200))
    return account


@pytest.mark.wip
def test_when_account_with_random_balance_is_credit_by_100_then_balance_should_be_increased_by_100(
        account_with_random_balance):
    account_init_balance = account_with_random_balance.get_balance()
    account_with_random_balance.credit(100)
    assert account_with_random_balance.get_balance() - account_init_balance == 100


def test_when_new_account_is_created_then_balance_is_0(account):
    assert account.get_balance() == 0, "The balance after account was created should be 0."


def test_when_new_account_is_credited_with_negative_value_then_valueerror_should_raise(account):
    with pytest.raises(ValueError):
        account.credit(100)


def test_when_new_account_is_credit_by_100_then_its_balance_should_be_100(account):
    account.credit(100)
    assert account.get_balance() == 100


@pytest.mark.parametrize('value', [1.23, 'jano', True, BankAccount(), list, None])
def test_when_wrong_type_is_credited_then_exception_TypeError_should_be_raised(account, value):
    with pytest.raises(TypeError):
        account.credit(value)
