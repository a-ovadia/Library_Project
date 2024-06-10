from Books import Book

# Collection of Books
class BookCollection:


    def __init__(self, book, number_available = 1, loaned = 0 ):
        self._book = book
        self._number_available = number_available
        self._number_loaned = loaned
        self._available = self._count - self._loaned
