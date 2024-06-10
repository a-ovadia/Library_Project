from Books import Book

# Collection of Books
class BookCollection:


    def __init__(self, book, total_count = 1, loaned = 0 ):
        self._book = book
        self._total_count = total_count
        self._number_loaned = loaned
        self._number_available = self._total_count - self._number_loaned
