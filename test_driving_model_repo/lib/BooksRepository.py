from lib.book import Book

class BooksRepository:
    def __init__(self,connection):
        self._connection = connection
    def all(self):
        books = []
        rows = self._connection.execute('SELECT * from books')
        for row in rows:
            data = Book(row['id'],row['title'],row['author_name'])
            books.append(data)
        return books