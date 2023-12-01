from lib.Tag import Tag

def test_init_correct():
    test_Tag = Tag(1,'Test Title')
    assert test_Tag.id == 1
    assert test_Tag.name == 'Test Title'
def test_format_correct():
    test_Tag = Tag(1,'Test Title')
    assert str(test_Tag) == 'Tag(1, Test Title)'
def test_object_test_passes():
    test_Tag = Tag(1,'Test Title')
    assert Tag(1,'Test Title') == test_Tag