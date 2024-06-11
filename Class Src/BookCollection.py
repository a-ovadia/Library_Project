from Books import Book

# Collection of Books
class BookCollection:
    
    # Constructors
    def __init__(self, book, total_count = 1, loaned = 0 ):
        """
        Represents a collection of Books
        
        Args:
            book (Book): Book in collection
            total_count (int): Total number of books
            loaned (int): Number of books loaned
        """
        if not isinstance(total_count, int):
            raise ValueError("total count must be an int")
        if not isinstance(loaned, int):
            raise ValueError("loaned must be an int")
        
        self._book = book
        self._total_count = total_count
        self._number_loaned = loaned

    def __repr__(self) -> str:
        return f"BookCollection(book = {self._book}, total count = {self._total_count}, number loaned = {self._number_loaned})"

    def set_book(self, book):
        self._book = book
    
    def set_total_count(self, total_count):
        self._total_count = total_count

    def set_number_loaned(self, loaned):
        self._number_loaned = loaned

    def get_book(self):
        return self._book
    
    def get_total_count(self):
        return self._total_count
    
    def get_number_loaned(self):
        return self._number_loaned
        
    @property
    def number_available(self):
        """
        Dynamically determine the number of books available to be loaned
        """
        return self._total_count - self._number_loaned

    def add_books(self, number_of_books):
        if number_of_books < 0:
            raise ValueError("You cannot add a negative value")
        self.set_total_count(self.get_total_count() + number_of_books) 
        return True
    
    def loan_book(self, number_of_books):
        if number_of_books < 0:
            raise ValueError("You cannot loan a negative quatity of books")
        if number_of_books > self.number_available:
            raise ValueError("There are not enough books available to loan")
        self.set_number_loaned(self.get_number_loaned() + number_of_books)
        return True

    def return_book(self, number_of_books):
        if number_of_books < 0:
            raise ValueError("You cannot return a negative quatity of books")
        if number_of_books > self.get_number_loaned():
            raise ValueError("You cannot return more books than are loaned")
        self.set_number_loaned(self.get_number_loaned() - number_of_books)
        return True
