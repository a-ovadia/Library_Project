from BookCollection import BookCollection
from Person import Person
from Books import Book

# Collection of a collection of books -> list of BookCollections
class Library:

    def __init__(self, book_collection : BookCollection):
        """
        Used to manage a list of BookCollection objects

        Args:
            book_collection list[BookCollection] - A BookCollection to append to the library list
        """
        self.validate_book_collections(book_collection)
        self._book_collection = book_collection
        

    def get_book_collection(self):
        return self._book_collection
    
    def validate_book_collections(self, book_collections):
        """
        Helper function to validate input is a list of type BookCollection

        Args:
            book_collection - Determine if this entry is a list of BookCollection objs
        """
        if not isinstance(book_collections, list):
            raise ValueError("Expected a list of BookCollection objects")
        for item in book_collections:
            if not isinstance(item, BookCollection):
                raise ValueError("All items in the list must be instances of BookCollection")



    def add_book_collections(self, book_collection):
        """
        Add a BookCollection to the Library

        Args:
            book_collection_list (BookCollection) - BookCollection to add
        """
        if not isinstance(book_collection, BookCollection):
            raise ValueError("Error. Library can only add BookCollection objs")
      
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

    def loan_book(self, loan_book : BookCollection, loan_person : Person):
        """
        Function to loan a book from the Library
        
        Args: 
            loan_book (Book) - The book to loan
            loan_person (Person) - Who is loaning the book
        
        """

        for book_collection in self._book_collection:
            if book_collection.get_book() == loan_book:
                if book_collection.loan_book(1):
                    loan_person.add_book(loan_book)
                    return True
                else:
                    raise ValueError("Book is not available")
        #raise ValueError("The book is not found in the collection")
    
    def return_book(self, loan_book, loan_person):
        """
        Function to return a loaned book back to the Library

        Args:
            loan_book (Book) - The book that was loaned
            loan_person (Person) - The person who loaned the book
        """
        # if not (isinstance(loan_person, Person) and isinstance(loan_book, BookCollection)):
        #     raise ValueError("Loan person and/or loan book have not been entered in the correct format")
        # if loan_book not in self._book_collection:
        #     raise ValueError("Error. The book is not in the library")
        
        for book in self._book_collection:
            if book.get_book() == loan_book:
                book.return_book(1)
                loan_book.remove_book(loan_book)
                return True
      #  raise ValueError("Book not found in the Collection")
    
    def print_library(self):
        for book_collection in self._book_collection:
            print(book_collection)

    def print_book_collection(self, book_collections):
        if not book_collections:
            print("The Collection is Empty")
            return False
        
        print("{:<30} {:<20} {:<15} {:<15} {:<15}".format("Title", "Author", "Genre", "Total Count", "Loaned"))
        for book_collection in book_collections:
            book = book_collection.get_book()
            print("{:<30} {:<20} {:<15} {:<15} {:<15}".format(
                        book.get_title(), book.get_author(), book.get_genre(), 
                        book_collection.get_total_count(), book_collection.get_number_loaned()
                    ))
    
    def is_book_available(self, book_title):
        for book_collect in self._book_collection:
            if book_title.lower() == book_collect.get_book().get_title().lower():
                if book_collect.number_available > 0:
                    return True
        return False
    
    def get_book(self, book_title):
        for book in self._book_collection:
            if book.get_book().get_title().lower() == book_title.lower():
                return book