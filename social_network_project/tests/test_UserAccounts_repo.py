from lib.Post import Post
from lib.useraccount import UserAccount
from lib.useraccounts import UserAccounts

def test_UserAccounts_returns_all_users(db_connection):
        
    db_connection.seed("seeds/social_media.sql")
    repository = UserAccounts(db_connection)
    result = repository.all_users()

    assert result == [
        UserAccount(1,'TestUsername1','testemailaddress@fakemail.com'),
        UserAccount(2,'TestUsername2','testemailaddress2@fakemail.com')
    ]

def test_UserAccounts_returns_posts_for_user(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = UserAccounts(db_connection)

    assert repository.posts_by_user(1) == [Post(1,'Test Title1', 'This is some test content',1337,1),Post(2,'Test Title2', 'This is some test content',1337,1)]

def test_UserAccounts_returns_single_post_for_user(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = UserAccounts(db_connection)

    assert repository.post_by_user(1,1) == Post(1,'Test Title1', 'This is some test content',1337,1)

def test_user_can_be_created(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = UserAccounts(db_connection)
    repository.create_user('TestUsername3','testemailaddress3@fakemail.com')
    result = repository.all_users()
    assert result == [
        UserAccount(1,'TestUsername1','testemailaddress@fakemail.com'),
        UserAccount(2,'TestUsername2','testemailaddress2@fakemail.com'),
        UserAccount(3,'TestUsername3','testemailaddress3@fakemail.com')
    ]
def test_user_can_create_post(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = UserAccounts(db_connection)
    repository.create_post(1,'Test Title3','This is some test content',1337)
    assert repository.posts_by_user(1) == [Post(1,'Test Title1', 'This is some test content',1337,1),Post(2,'Test Title2', 'This is some test content',1337,1),Post(5,'Test Title3', 'This is some test content',1337,1)]
