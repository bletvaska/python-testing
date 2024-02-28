import pytest
from pydantic import BaseModel


class BankAccount(BaseModel):
    balance: int = 0

    def get_balance(self):
        return self.balance

    def deposit(self, amount: int):
        if type(amount) is not int:
            raise TypeError('Amount is not an integer.')
        if amount <= 0:
            raise ValueError("Invalid amount.")

        self.balance = amount


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
# ked vyberiem viac ako je zostatok, tak ValueError
# ked zadam zapornu hodnotu, tak vynimka ValueError
# ked zadam iny typ ako cele cislo, tak TypeError

