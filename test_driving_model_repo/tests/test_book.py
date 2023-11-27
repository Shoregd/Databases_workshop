from lib.book import Book

def test_init_correct_values():
    test_book = Book(1,'Test Title','Test Author')
    assert test_book.id == 1
    assert test_book.title == 'Test Title'
    assert test_book.author_name == 'Test Author'

def test_repr_returns_correctly():
    test_book = Book(1,'Test Title','Test Author')
    assert str(test_book) == 'Book: 1, Test Title, Test Author'

def test_book_classes_equivalent():
    test_book = Book(1,'Test Title','Test Author')
    test_book2 = Book(1,'Test Title','Test Author')
    assert test_book == test_book2