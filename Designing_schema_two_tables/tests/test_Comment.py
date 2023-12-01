from lib.Comment import Comment

def test_init_correct():
    test_Comment = Comment(1,'Greg Bloggs','This is some test content',1)
    assert test_Comment.id == 1
    assert test_Comment.author_name == 'Greg Bloggs'
    assert test_Comment.content == 'This is some test content'
    assert test_Comment.post_id == 1

def test_format_correct():
    test_Comment = Comment(1,'Greg Bloggs','This is some test content',1)
    assert str(test_Comment) == 'Comment(1, Greg Bloggs, This is some test content, 1)'

def test_eqtesting_correct():
    test_Comment = Comment(1,'Greg Bloggs','This is some test content',1)
    assert test_Comment == Comment(1,'Greg Bloggs','This is some test content',1)