Set up a new project called book_store from the starter.
Use the book_store SQL seed instead of the music_library seed. You can find this in the seeds directory in the starter.
Follow the design recipe as usual, before starting to test-drive the classes.
Once you've done the design recipe, start recording yourself.
Test-drive a Book class that has attributes for each column in the books table, using the example(s) from your design.
Test-drive a BookRepository class that has a method all that returns a list of Book objects.
Write a small program in app.py using the class BookRepository to print out the list of books to the terminal.


--- Design Recipe ---

Design and create the table if needed. - Tables have been pre-created
Create test SQL seeds. - SQL seeds have been provided
Define the Model and Repository class names. - Completed
Implement the Model class. - Completed
Design the Repository class interface. -
Write test examples.
Test-drive and implement the Repository class behaviour.


--- Model and Repository Class names. ---

* Book
    * ID - system determined
    * title
    * author_name


* BookRepository
    * init - starting connection to the database.
    * all function return a list of the books.