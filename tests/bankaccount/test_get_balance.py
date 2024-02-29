def test_when_account_is_created_then_balance_is_0(account):
    assert account.get_balance() == 0, 'When created, then balance should be 0.'
