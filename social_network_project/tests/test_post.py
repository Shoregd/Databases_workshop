from lib.Post import Post

def test_init_correct():
    test_post = Post(1,'Test Title','This is some test contents.',1337,1)
    assert test_post.id ==1
    assert test_post.title == 'Test Title'
    assert test_post.contents == 'This is some test contents.'
    assert test_post.views ==1337
    assert test_post.useraccount_id ==1

def test_repr_format():
    test_post = Post(1,'Test Title','This is some test contents.',1337,1)

    assert str(test_post) == 'Post(1, Test Title, This is some test contents., 1337, 1)'

def test_eq_for_later_tests():
    test_post = Post(1,'Test Title','This is some test contents.',1337,1)
    test_post2 = Post(1,'Test Title','This is some test contents.',1337,1)
    assert test_post == test_post2