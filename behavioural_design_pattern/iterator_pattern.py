"""
GPT

The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object (e.g., a collection) sequentially without exposing its underlying representation. This pattern allows clients to traverse a collection in a standard way, regardless of its internal structure.
Example: Custom Collection with Iterator

Let’s implement a custom collection called BookCollection that holds books. We'll also create an iterator that allows us to traverse the collection in a sequential manner.

GPT

The Iterator Pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object (e.g., a collection) sequentially without exposing its underlying representation. This pattern allows clients to traverse a collection in a standard way, regardless of its internal structure.
Example: Custom Collection with Iterator

Let’s implement a custom collection called BookCollection that holds books. We'll also create an iterator that allows us to traverse the collection in a sequential manner.
Code Example:

python

from collections.abc import Iterable, Iterator

# Book class (individual elements in the collection)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Custom Iterator for the BookCollection
class BookIterator(Iterator):
    def __init__(self, book_list):
        self._book_list = book_list
        self._index = 0

    def __next__(self):
        if self._index < len(self._book_list):
            book = self._book_list[self._index]
            self._index += 1
            return book
        raise StopIteration

# Custom Collection that is Iterable
class BookCollection(Iterable):
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

# Client Code
def client_code():
    # Create a book collection
    collection = BookCollection()
    collection.add_book(Book("1984", "George Orwell"))
    collection.add_book(Book("Brave New World", "Aldous Huxley"))
    collection.add_book(Book("Fahrenheit 451", "Ray Bradbury"))

    # Iterate over the book collection using the iterator
    print("Iterating through the book collection:")
    for book in collection:
        print(book)

# Usage
client_code()

Explanation:

    Book Class (Element):
        Represents the individual elements stored in the collection, in this case, a Book with a title and author.

    BookIterator (Iterator):
        Implements the Iterator interface, with the __next__() method.
        Keeps track of the current position in the list (_index) and returns the next book on each call to __next__(). If the collection is fully traversed, it raises StopIteration, which is standard behavior for iterators.

    BookCollection (Iterable):
        Implements the Iterable interface by defining the __iter__() method, which returns a BookIterator object. This allows the collection to be traversed using a for loop or other iteration mechanisms.
        Contains a list of Book objects and allows adding new books via the add_book() method.

    Client Code:
        The client interacts with BookCollection using a for loop. Behind the scenes, the __iter__() method of the collection is called, which provides an iterator that allows sequential access to each Book.
"""
from collections.abc import Iterable, Iterator

# Book class (individual elements in the collection)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Custom Iterator for the BookCollection
class BookIterator(Iterator):
    def __init__(self, book_list):
        self._book_list = book_list
        self._index = 0

    def __next__(self):
        if self._index < len(self._book_list):
            book = self._book_list[self._index]
            self._index += 1
            return book
        raise StopIteration

# Custom Collection that is Iterable
class BookCollection(Iterable):
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

# Client Code
def client_code():
    # Create a book collection
    collection = BookCollection()
    collection.add_book(Book("1984", "George Orwell"))
    collection.add_book(Book("Brave New World", "Aldous Huxley"))
    collection.add_book(Book("Fahrenheit 451", "Ray Bradbury"))

    # Iterate over the book collection using the iterator
    print("Iterating through the book collection:")
    for book in collection:
        print(book)

# Usage
client_code()
