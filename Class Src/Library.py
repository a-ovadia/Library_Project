from Books import Book

# Collection of Books
class BookCollection:


    def __init__(self, book = None, count = 1, loaned = 0 ):
        self._book = book
        self._count = count
        self._loaned = loaned
        self._available = self._count - self._loaned


    d