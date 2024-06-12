import PrintOut
from LibraryCard import LibraryCard
from datetime import datetime

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
    
    def set_person(self, person):
        self._person = person

    def get_library(self):
        return self._library
    
    def get_person(self):
        return self._person
    
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
                    
                    # If person does not have a Library card, issue one
                    if not person.get_library_card():
                        person.add_library_card(LibraryCard())   

                    # Check expiration date of library card
                    elif datetime.now() >= person.get_library_card().expiration_date:
                        print("Need to renew library card") # Will implement later

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
            print("1. Search Library")
            print("2. Check if a book is available")
            print("3. Loan a book")
            print("4. Print Status Menu")
            print("5. Return book")
       
            selection = input("Enter Selection choice: ")



            # Search Library
            if selection == "1":
                search_term = input("Enter search term: ")
                search_by = input("Enter filter to search by: Enter 't' for Title, 'a' for author, 'i' for isbn, 'd' for publication date, 'g' for genre, 'p' for publisher")
                self.print_book_collection(self.search_library(search_term, search_by))

            
            elif selection == "2":
                book_title = input("Enter the title of the book: ")
                print(self.is_book_available(book_title))

            elif selection == "3":
                book_title = input("Enter the book title you would like to loan: ").lower()
                self.loan_book(book_title)
                
            
            elif selection == "4":
                print_selection = None
                while print_selection != "c":
                    print("1. Print loan books")
                    print("2. Print loans for a person")
                    print("3. Print all books")
                    print("4. Print only available books")
                    print("5. Print person list")
                    print("6. Print overdue books")
                    print("c: MAIN MENU")
                    print_selection = input("Enter selection: ").lower()
                
                    if print_selection == "1":
                        PrintOut.print_loaned_books(self.get_person())
                    
                    elif print_selection == "2":
                        name = input("Please enter your name: ")
                        for entry in self._person:
                            if entry.get_name().lower() == name.lower():
                                PrintOut.print_loans_for_person(entry)

                    elif print_selection == "3":
                        PrintOut.print_all_books(self)

                    elif print_selection == "4":
                        PrintOut.print_available_books(self)

                    elif print_selection == "5":
                        PrintOut.print_person_list(self)

                    elif print_selection == "6":
                        PrintOut.print_overdue_books(self)

            elif selection == "5":
                name = input("Enter your name: ").lower()
                for person in range(len(self.get_person())):
                    if name.lower() == self._person[person].get_name().lower():
                        PrintOut.print_loans_for_person(self._person[person])


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