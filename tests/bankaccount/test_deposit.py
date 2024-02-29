import pytest

from training.bankaccount import BankAccount


def test_when_deposited_100_evry_then_balance_is_100_evry(account):
    # act
    account.deposit(100)

    # assert
    assert account.get_balance() == 100, \
        'Whend deposited 100 evry, then balance should be 100 evry'


def test_when_negative_balance_deposit_then_exception_should_be_raised(account):
    with pytest.raises(ValueError):
        account.deposit(-100)

@pytest.mark.parametrize('amount', [True, False, None, [], {}, 132.45, 'jano', (), BankAccount])
def test_when_invalid_type_of_amount_then_type_error_should_be_raised(amount, account):
    with pytest.raises(TypeError):
        account.deposit(amount)
