from Books import Book
from LibraryCard import LibraryCard

class Person:

    def __init__(self, name, library_card = None, genre = "", books = None, email = None, phone = None):
        self._name = name
        self._favorite_genre = genre
        self._loaned_books = books if books is not None else []
        self._library_card = library_card
        self._email = email
        self._phone = phone

    def __repr__(self):
        return (f"Person(name={self._name!r}, library_card={self._library_card!r}, "
                f"favorite_genre={self._favorite_genre!r}, loaned_books={self._loaned_books!r}, "
                f"email={self._email!r}, phone={self._phone!r})")
    
    # Define setters
    def set_name(self, name):
        self._name = name

    def add_library_card(self, library_card):
        if not isinstance(library_card, LibraryCard):
            raise ValueError("Library card must be of type LibraryCard")
        self._library_card = library_card
    
    def set_favorite_genre(self, genre):
        self._favorite_genre = genre

    def add_book(self, book : Book):
        self._loaned_books.append(book)

    def remove_book(self, book : Book):
        self._loaned_books.remove(book)
    
    def set_email(self, email):
        self._email = email
    
    def set_phone(self, phone):
        self._phone = phone
        
    
    # Define getters
    def get_name(self):
        return self._name

    def get_library_card(self):
        return self._library_card
    
    def get_favorite_genre(self):
        return self._favorite_genre
    
    def get_loaned_books(self):
        return self._loaned_books

    def get_email(self):
        return self._email
    
    def get_phone(self):
        return self._phone
    
    # Returns True if the person has loaned the book, False otherwise
    def has_loaned_book(self, bookc):
        for item in self._loaned_books:
            if item.get_title().lower() == bookc.get_book().get_title().lower():
                return True
        return False