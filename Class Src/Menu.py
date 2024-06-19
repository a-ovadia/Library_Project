import PrintOut
from LibraryManager import LibraryManager


def main_menu(LibMan : LibraryManager):
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
                search_term = input("Enter search term: ").lower()
                if not search_term:
                    print("Error. Please enter a search term")
                    continue
                valid_search_term = ["t", "a", "i", "d", "g", "p"]
                search_by = input("Enter filter to search by: Enter 't' for Title, 'a' for author, 'i' for isbn, 'd' for publication date, 'g' for genre, 'p' for publisher").strip().lower()
                if search_by not in valid_search_term:
                    print("Error. You did not enter a valid search filter")
                    continue
                LibMan.print_book_collection(LibMan.search_library(search_term, search_by))

            
            elif selection == "2":
                book_title = input("Enter the title of the book: ").lower()
                if not book_title:
                    print("Error. You did not enter a book title to search")
                    continue
                print(LibMan.is_book_available(book_title))

            elif selection == "3":
                book_title = input("Enter the book title you would like to loan: ").lower()
                if not book_title:
                    print("Error. You did not enter a book title to search")
                    continue
                LibMan.loan_book(book_title)
                
            
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
                    print_selection = input("Enter selection: ").strip().lower()
                
                    if print_selection == "1":
                        PrintOut.print_loaned_books(LibMan.get_person())
                    
                    elif print_selection == "2":
                        name = input("Please enter your name: ").lower()
                        if not name:
                            print("Error. You have not entered your name")
                            continue
                        for entry in LibMan._person:
                            if entry.get_name().lower() == name:
                                PrintOut.print_loans_for_person(entry)

                    elif print_selection == "3":
                        PrintOut.print_all_books(LibMan)

                    elif print_selection == "4":
                        PrintOut.print_available_books(LibMan)

                    elif print_selection == "5":
                        PrintOut.print_person_list(LibMan)

                    elif print_selection == "6":
                        PrintOut.print_overdue_books(LibMan)

            elif selection == "5":
                name = input("Enter your name: ").lower()
                if not name:
                    print("Error. You have not entered a valid name")
                    continue
                person_list = LibMan.get_person()
                loan_person = None
                for person in person_list:
                    if name.lower() == person.get_name().lower():
                        PrintOut.print_loans_for_person(person)
                        loan_person = person
                book = input("Enter book title: ").lower()
                book_obj = LibMan.get_library().get_book(book)
                if book_obj:
                    print("Returning book")
                LibMan.return_loaned_book(loan_person, book_obj)