import pytest

from bank.bankaccount import BankAccount


@pytest.fixture
def empty_bankaccount(faker):
    """
    Creates empty BankAccount object.
    """
    account = BankAccount(owner=faker.name())
    yield account
