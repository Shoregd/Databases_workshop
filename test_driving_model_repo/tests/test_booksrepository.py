from lib.BooksRepository import BooksRepository
from lib.book import Book
book1= Book(1,'Test Title','Test Author')
book2= Book(2,'Test Title','Test Author')
book3= Book(3,'Test Title','Test Author')
book4= Book(4,'Test Title','Test Author')
#def test_init_accepts_books_and_stores():
#    test_repo = BooksRepository(book1,book2,book3,book4)
#    assert test_repo.booklist == [book1,book2,book3,book4]

#def test_all_returns_repr_of_books():
#    test_repo = BooksRepository(book1,book2,book3,book4)
#    assert test_repo.all() == f'{str(book1)}\n{str(book2)}\n{str(book3)}\n{str(book4)}'