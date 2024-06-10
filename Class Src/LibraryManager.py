from Library import Library
from Books import Book
from Person import Person
from BookCollection import BookCollection


# From the perspective of a Librarian
# Interface between Library and user input 
class LibraryManager:

    def __init__(self, library : Library):
        self._library = library

    def set_library(self, library):
        self._library = library

    def get_library(self):
        return self._library
    
    def print_book_collection(self, book_collection):
        self._library.print_book_collection(book_collection)

    def main_menu(self):
        print("Main Menu")
        print("1. View all books in the library")
        print("2. Search Library")
        selection = input("Enter Selection choice: ")

        while True:

            if selection == "2":
                search_term = input("Enter search term: ")
                search_by = input("Enter filter to search by: Enter 't' for Title, 'a' for author, 'i' for isbn, 'd' for publication date, 'g' for genre, 'p' for publisher")
                print(self.search_library(search_term, search_by))

    def view_all_books(self):
        self._library.print_library()

    
    def search_library(self, search_term, search_option = "t"):
        result_list = None
        if not search_term:
            raise ValueError("The search term cannot be empty")
        search_term = search_term.lower().strip()
        
        if search_option.lower() == "t":
            result_list = self.helper_search_library_opt_t(search_term)

        elif search_option.lower() == "i":
            result_list = self.helper_search_library_opt_i(search_term)

        elif search_option.lower() == "a":
            result_list = self.helper_search_library_opt_a(search_term)

        elif search_option.lower() == "d":
            result_list = self.helper_search_library_opt_d(search_term)

        elif search_option.lower() == "g":
            result_list = self.helper_search_library_opt_g(search_term)

        elif search_option.lower() == "p":
            result_list = self.helper_search_library_opt_p(search_term)
        return result_list

    # Helper functions for search
    def helper_search_library_opt_t(self, search_term):
        result_list = []
        for book_collection in self._library._book_collection:
            book = book_collection.get_book()
            if search_term in book.get_title().lower():
                result_list.append(book_collection)
        return result_list

    def helper_search_library_opt_i(self, search_term):
        result_list = []
        for book_collection in self._library._book_collection:
            book = book_collection.get_book()
            if search_term in book.get_isbn().lower():
                result_list.append(book_collection)
        return result_list
    
    def helper_search_library_opt_a(self, search_term):
        result_list = []
        for book_collection in self._library._book_collection:
            book = book_collection.get_book()
            if search_term in book.get_author().lower():
                result_list.append(book_collection)
        return result_list
    
    def helper_search_library_opt_d(self, search_term):
        result_list = []
        for book_collection in self._library._book_collection:
            book = book_collection.get_book()
            if search_term in book.get_publication_date().lower():
                result_list.append(book_collection)
        return result_list
    
    def helper_search_library_opt_g(self, search_term):
        result_list = []
        for book_collection in self._library._book_collection:
            book = book_collection.get_book()
            if search_term in book.get_genre().lower():
                result_list.append(book_collection)
        return result_list        

    def helper_search_library_opt_p(self, search_term):
        result_list = []
        for book_collection in self._library._book_collection:
            book = book_collection.get_book()
            if search_term in book.get_publisher().lower():
                result_list.append(book_collection)
        return result_list        
