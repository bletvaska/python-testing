# ked vyberiem 100 evry, tak na ucte budem mat o 100 evry menej
import pytest

from training.bankaccount import BankAccount


def test_when_withdraw_100_then_balance_should_be_100_evry_less(account):
    # arrange
    account.deposit(200)

    # act
    account.withdraw(100)

    # assert
    assert account.get_balance() == 100


# ked vyberiem viac ako je zostatok, tak ValueError
def test_when_no_funds_on_account_when_withdraw_then_valueerror_exception_should_be_raised(account):
    with pytest.raises(ValueError):
        account.withdraw(10)


# ked zadam zapornu hodnotu, tak vynimka ValueError
def test_when_negative_balance_withdraw_then_exception_should_be_raised(account):
    with pytest.raises(ValueError):
        account.withdraw(-100)


# ked zadam iny typ ako cele cislo, tak TypeError
@pytest.mark.parametrize('amount', [True, False, None, [], {}, 132.45, 'jano', (), BankAccount])
def test_when_invalid_type_of_amount_withdrawed_then_type_error_should_be_raised(amount, account):
    with pytest.raises(TypeError):
        account.withdraw(amount)


def test_when_0_amount_is_withdraw_then_valueerror_should_be_raised(account):
    account.deposit(100)
    with pytest.raises(ValueError):
        account.withdraw(0)
