def test_when_account_was_created_then_balance_is_0(empty_bankaccount):
    # assert
    assert empty_bankaccount.balance == 0, "Balance should be 0 when account was created."
