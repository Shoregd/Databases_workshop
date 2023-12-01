from lib.Post import Post

def test_init_correct():
    test_post = Post(1,'Test Title')
    assert test_post.id == 1
    assert test_post.title == 'Test Title'
def test_format_correct():
    test_post = Post(1,'Test Title')
    assert str(test_post) == 'Post(1, Test Title)'
def test_object_test_passes():
    test_post = Post(1,'Test Title')
    assert Post(1,'Test Title') == test_post
