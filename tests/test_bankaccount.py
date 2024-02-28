import pytest

from training.bankaccount import BankAccount


@pytest.fixture()
def account():
    # setup
    account = BankAccount()
    yield account
    # teardown


def test_when_account_is_created_then_balance_is_0(account):
    assert account.get_balance() == 0, 'When created, then balance should be 0.'


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


# ked vyberiem 100 evry, tak na ucte budem mat o 100 evry menej
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
# ked zadam iny typ ako cele cislo, tak TypeError
