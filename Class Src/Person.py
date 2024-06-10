from Books import Book
from LibraryCard import LibraryCard

class Person:

    def __init__(self, name, library_card = None, genre = "", books = None):
        self._name = name
        self._favorite_genre = genre
        self._loaned_books = [books]
        self._library_card = library_card

    # Define setters
    def set_name(self, name):
        self._name = name

    def add_library_card(self, library_card):
        if not isinstance(library_card, LibraryCard):
            raise ValueError("Library card must be of type LibraryCard")
        self._library_card_number = library_card
    
    def set_favorite_genre(self, genre):
        self._favorite_genre = genre

    def add_book(self, book : Book):
        self._loaned_books.append(book)

    def remove_book(self, book : Book):
        self._loaned_books.remove(book)
    

    # Define getters
    def get_name(self):
        return self._name

    def get_library_card(self):
        return self._library_card_number
    
    def get_favorite_genre(self):
        return self._favorite_genre
    
    def get_loaned_books(self):
        return self._loaned_books
