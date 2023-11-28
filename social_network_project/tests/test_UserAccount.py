from lib.useraccount import UserAccount

def test_init_correct():
    test_UserAccount = UserAccount(1,'TestUsername','Thisisatestemail@fakemail.com')
    assert test_UserAccount.id ==1
    assert test_UserAccount.username == 'TestUsername'
    assert test_UserAccount.email_address == 'Thisisatestemail@fakemail.com'
   

def test_repr_format():
    test_UserAccount = UserAccount(1,'TestUsername','Thisisatestemail@fakemail.com')

    assert str(test_UserAccount) == 'UserAccount(1, TestUsername, Thisisatestemail@fakemail.com)'

def test_eq_for_later_tests():
    test_UserAccount = UserAccount(1,'TestUsername','Thisisatestemail@fakemail.com')
    test_UserAccount2 = UserAccount(1,'TestUsername','Thisisatestemail@fakemail.com')
    assert test_UserAccount == test_UserAccount2