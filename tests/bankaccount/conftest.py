import pytest

from training.bankaccount import BankAccount


@pytest.fixture()
def account():
    # setup
    account = BankAccount()
    yield account
    # teardown
