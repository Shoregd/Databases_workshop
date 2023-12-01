from lib.Post import Post

def test_init_correct():
    test_post = Post(1,'Test Title','This is some test content')
    assert test_post.id == 1
    assert test_post.title == 'Test Title'
    assert test_post.content == 'This is some test content'

def test_format_correct():
    test_post = Post(1,'Test Title','This is some test content')
    assert str(test_post) == 'Post(1, Test Title, This is some test content)'

def test_eqtesting_correct():
    test_post = Post(1,'Test Title','This is some test content')
    assert test_post == Post(1,'Test Title','This is some test content')