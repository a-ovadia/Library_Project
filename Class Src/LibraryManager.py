import PrintOut

"""
Todo: Start Person addition
- need to be able to check a person for a valid library card
  (number exists and not expired)
- Be able to issue a new library card

"""


from Library import Library
from Books import Book
from Person import Person
from BookCollection import BookCollection
from LibraryCard import LibraryCard

# From the perspective of a Librarian
# Interface between Library and user input 
class LibraryManager:

    def __init__(self, library : Library):
        self._library = library
        self._person = []

    def set_library(self, library):
        self._library = library

    def get_library(self):
        return self._library
    
    def print_book_collection(self, book_collection):
        self._library.print_book_collection(book_collection)


    def is_book_available(self, book_title):
        return self._library.is_book_available(book_title)
    
    def is_person_in_library(self, person_name):
        return person_name.lower() in (name.get_name().lower() for name in self._person)    
    
    def loan_book(self, book_title):
        # Check that book exists and is available
        if not self.is_book_available(book_title.lower()):
            print("Error. The requested book is not available")
            return False
        
        loan_person_name = input("Enter your name: ")
        book_loanc = None
        for book in self._library._book_collection:
            if book.get_book().get_title().lower() == book_title:
                book_loanc = book

        # Check if person exists
        if self.is_person_in_library(loan_person_name.lower()):
            # check if person already loaned this book 
            person = None
            
            for item in range(len(self._person)):
                if loan_person_name.lower() == self._person[item].get_name().lower():
                    person = self._person[item]
                    
                    # if person has not loaned the book before
                    if not person.has_loaned_book(book_loanc):
                        # loan book
                        return self.helper_loan_book(book_loanc, person)
                    else:
                        print("Error. You already have loaned this book")
                        return False
                    
        # Create new person if loaner is not in db
        new_person = self.create_new_person(loan_person_name)
        self._person.append(new_person)
        self.helper_loan_book(book_loanc, new_person)
        return True

    def create_new_person(self, name):
        genre = input("Enter favorite genre: ")
        email = input("Enter your email address: ")
        phone = input("Enter your phone number: ")
        new_person = Person(name.title(), genre=genre, email=email, phone=phone)
        lc = LibraryCard()
        new_person.add_library_card(lc)
        return new_person



    # Assumes valid Person and valid Book and Book is available
    def helper_loan_book(self, book : BookCollection, person : Person):
        book.set_number_loaned(book.get_number_loaned() + 1)
        person._loaned_books.append(book.get_book())
        return True

    def main_menu(self):
        while True:
            print("Main Menu")
            print("1. View all books in the library")
            print("2. Search Library")
            print("3. Check if a book is available")
            print("4. Loan a book")
            print("5. Check library loan status")
            selection = input("Enter Selection choice: ")

        
            # Print out entire contents of Library
            if selection == "1":
                self.print_book_collection(self._library.get_book_collection())

            # Search Library
            elif selection == "2":
                search_term = input("Enter search term: ")
                search_by = input("Enter filter to search by: Enter 't' for Title, 'a' for author, 'i' for isbn, 'd' for publication date, 'g' for genre, 'p' for publisher")
                self.print_book_collection(self.search_library(search_term, search_by))

            
            elif selection == "3":
                book_title = input("Enter the title of the book: ")
                print(self.is_book_available(book_title))

            elif selection == "4":
                book_title = input("Enter the book title you would like to loan: ").lower()
                self.loan_book(book_title)
                
            
            elif selection == "5":
                self.print_loaner_list()


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


    def print_loaner_list(self):
        #print(self._person)
        PrintOut.print_loaned_books(self._person)