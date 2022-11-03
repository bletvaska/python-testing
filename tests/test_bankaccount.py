from faker import Faker
import pytest

from bank.bankaccount import BankAccount

faker = Faker()


@pytest.fixture
def empty_bankaccount():
    account = BankAccount(owner=faker.name())
    yield account


def test_when_account_was_created_then_balance_is_0(empty_bankaccount):
    # assert
    assert empty_bankaccount.balance == 0, "Balance should be 0 when account was created."


def test_when_100_is_added_to_empty_account_then_balance_should_be_100(empty_bankaccount):
    # act
    empty_bankaccount.deposit(100)

    # assert
    assert empty_bankaccount.balance == 100, "Balance should be 100."


def test_when_deposit_to_account_with_nonzero_balance_then_final_balance_is_higher(empty_bankaccount):
    # arrange
    old_balance = faker.random_int(10, 1000)
    deposit = faker.random_int(10, 1000)
    empty_bankaccount.deposit(old_balance)

    # act
    empty_bankaccount.deposit(deposit)

    # assert
    assert empty_bankaccount.balance == old_balance + deposit, f"Balance should be {old_balance + deposit}."


def test_when_negative_amount_is_deposited_then_valueerror_exception_should_be_thrown(empty_bankaccount):
    # arrange
    amount = -100

    # act + assert
    with pytest.raises(ValueError):
        empty_bankaccount.deposit(amount)


@pytest.mark.parametrize("amount",[True, 12.3, "jano", BankAccount(owner="jano"), {}, [], (0,),])
def test_when_non_integer_type_is_deposited_then_expect_typeerror_exception(amount, empty_bankaccount):
    # act + assert
    with pytest.raises(TypeError):
        empty_bankaccount.deposit(amount)


# ak vyberiem z uctu 100 evry, tak sa zostatok znizi o 100 evry
def test_when_withdrawing_100_then_balance_will_decrease_of_100(empty_bankaccount):
    # arrange
    empty_bankaccount.balance = 200

    # act
    empty_bankaccount.withdraw(100)

    # assert
    assert empty_bankaccount.balance == 100


# ak zadam zapornu sumu, tak vyvolam vynimku ValueError
def test_when_negative_amount_is_withdrawn_then_valueerror_exception_should_be_thrown(empty_bankaccount):
    # arrange
    amount = -100

    # act + assert
    with pytest.raises(ValueError):
        empty_bankaccount.withdraw(amount)


# ak zadam iny typ ako celé číslo, tak skoncim s výnimkou TypeError
@pytest.mark.parametrize("amount",[True, 12.3, "jano", BankAccount(owner="jano"), {}, [], (0,), None])
def test_when_non_integer_type_is_withdrawn_then_expect_typeerror_exception(amount, empty_bankaccount):
    # act + assert
    with pytest.raises(TypeError):
        empty_bankaccount.withdraw(amount)


# ak sa pokusim o vyber vacsieho mnozstva penazi, ako je zostatok, tak ValueError
def test_when_greater_amount_of_money_is_withdrawn_than_balance_then_except_valueerror_exception(empty_bankaccount):
    with pytest.raises(ValueError):
        empty_bankaccount.withdraw(1)


# ak sa vyberiem  rovnakú sumu, ako je zostatok na ucte, tak vysledny zostatok bude 0
def test_when_balance_is_withdrawn_then_balance_should_be_0(empty_bankaccount):
    # arange
    empty_bankaccount.balance = 100

    # act
    empty_bankaccount.withdraw(100)

    # assert
    assert empty_bankaccount.balance == 0


# ak zadam 0, tak skoncim s výnimkou ValueError
def test_when_0_is_withdrawn_then_expect_valuerror_exception(empty_bankaccount):
    with pytest.raises(ValueError):
        empty_bankaccount.withdraw(0)

