from datetime import datetime

class Book:

    def __init__(self, book_title, book_author, book_isbn, book_publication_date = None, book_genre = "", book_publisher = "", book_summary = ""):
        self._title = book_title
        self._author = book_author
        self._isbn = book_isbn
        self._publication_date = book_publication_date
        self._genre = book_genre
        self._publisher = book_publisher
        self._summary = book_summary

    def __repr__(self):
        return (f"Book(title={self._title}, author={self._author}, isbn={self._isbn}, "
                        f"publication_date={self._publication_date}, genre={self._genre}, "
                        f"publisher={self._publisher}, summary={self._summary})")
    
    # Define setter methods
    def set_title(self, book_title):
        if not book_title:
            raise ValueError("Book title cannot be empty")
        self._title = book_title
    def set_author(self, book_author):
        if not book_author:
            raise ValueError("Book author cannot be empty")
        self._author = book_author
    def set_isbn(self, book_isbn):
        if not book_isbn:
            raise ValueError("book ISBN cannot be empty")
        self._isbn = book_isbn
    def set_publication_date(self, book_publication_date):
        if not isinstance(book_publication_date, datetime) and not book_publication_date is None:
            raise TypeError("Publication date must be a DateTime Object")
        self._publication_date = book_publication_date
    def set_genre(self, book_genre):
        self._genre = book_genre
    def set_publisher(self, book_publisher):
        self._publisher = book_publisher
    def set_summary(self, book_summary):
        self._summary = book_summary
    
    # Define getter methods
    def get_title(self):
        return self._title
    def get_author(self):
        return self._author
    def get_isbn(self):
        return self._isbn
    def get_publication_date(self):
        return self._publication_date
    def get_genre(self):
        return self._genre
    def get_publisher(self):
        return self._publisher
    def get_summary(self):
        return self._summary
    