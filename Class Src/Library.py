from BookCollection import BookCollection
from Person import Person
from Books import Book

# Collection of a collection of books -> list of BookCollections
class Library:

    def __init__(self, book_collection : BookCollection):
        """
        Used to manage a list of BookCollection objects

        Args:
            book_collection (BookCollection) - A BookCollection to append to the library list
        """
        self._book_collection = [book_collection]
        

    def add_book_collections(self, book_collection_list):
        """
        Add a BookCollection to the Library

        Args:
            book_collection_list (BookCollection) - BookCollection to add
        """
        if not isinstance(book_collection_list, BookCollection):
            raise ValueError("Error. Library can only add BookCollection objs")
        for book_collection in book_collection_list:
            self._book_collection.append(book_collection)

    def is_book_in_collection(self, book : Book):
        """
        Checks if a Book exists in BooksCollection library

        Args:
            book (Book) - A book to check if it exists

        Returns:
            True - If book is found
            False - If book is not found
        """
        for book_obj in self._book_collection:
            if book_obj.get_book() == book:
                return True
        return False

    def loan_book(self, loan_book : Book, loan_person : Person):
        """
        Function to loan a book from the Library
        
        Args: 
            loan_book (Book) - The book to loan
            loan_person (Person) - Who is loaning the book
        
        """
        if not self.is_book_in_collection(loan_book):
            raise ValueError("Error. The book is not in the library")
        if not isinstance(loan_person, Person):
            raise ValueError("Error the requested loaner must be a Person Obj")
        for book_collection in self._book_collection:
            if book_collection.get_book() == loan_book:
                if book_collection.loan_book(1):
                    loan_person.add_book(loan_book)
                    return True
                else:
                    raise ValueError("Book is not available")
        raise ValueError("The book is not found in the collection")
    
    def return_book(self, loan_book, loan_person):
        """
        Function to returna loaned book back to the Library

        Args:
            loan_book (Book) - The book that was loaned
            loan_person (Person) - The person who loaned the book
        """
        if loan_book not in self._book_collection:
            raise ValueError("Error. The book is not in the library")
        if not isinstance(loan_person, Person):
            raise ValueError("Error the requested loaner must be a Person Obj")
        for book in self._book_collection:
            if book.get_book() == loan_book:
                book.return_book(1)
                loan_book.remove_book(loan_book)
                return True
        raise ValueError("Book not found in the Collection")