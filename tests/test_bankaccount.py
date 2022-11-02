import pytest

from bank.bankaccount import BankAccount


@pytest.fixture
def empty_bankaccount():
    account = BankAccount(owner="janko hrasko")
    yield account


def test_when_account_was_created_then_balance_is_0(empty_bankaccount):
    # assert
    assert (
        empty_bankaccount.balance == 0
    ), "Balance should be 0 when account was created."


def test_when_100_is_added_to_empty_account_then_balance_should_be_100(
    empty_bankaccount,
):
    # act
    empty_bankaccount.deposit(100)

    # assert
    assert empty_bankaccount.balance == 100, "Balance should be 100."


def test_when_deposit_to_account_with_nonzero_balance_then_final_balance_is_higher(
    empty_bankaccount,
):
    # arrange
    old_balance = 50
    deposit = 80
    empty_bankaccount.deposit(old_balance)

    # act
    empty_bankaccount.deposit(deposit)

    # assert
    assert (
        empty_bankaccount.balance == old_balance + deposit
    ), f"Balance should be {old_balance + deposit}."


def test_when_negative_amount_is_deposited_then_valueerror_exception_should_be_thrown(empty_bankaccount):
    # arrange
    amount = -100

    # act + assert
    with pytest.raises(ValueError):
        empty_bankaccount.deposit(amount)


@pytest.mark.wip
@pytest.mark.parametrize(
    "amount",
    [
        True,
        12.3,
        "jano",
        BankAccount(owner="jano"),
        {},
        [],
        (0,),
    ],
)
def test_when_non_integer_type_is_deposited_then_expect_typeerror_exception(amount, empty_bankaccount):
    # act + assert
    with pytest.raises(TypeError):
        empty_bankaccount.deposit(amount)

