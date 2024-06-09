import datetime as dt
import sys

# Initialize Library and loan data structures
library = {}
loan = {}

# Function to add a book to the Library
# Return True if successful, Otherwise False if error
def add_book_to_library(book_title, book_author, 
                        book_isbn, book_count = 1):
    
    # Set to Title format
    book_title = book_title.title()
    book_author = book_author.title()

    """
        Input validation:
            Book_title is string, book_title already exists
            Book_author is string
            return current book count if book exists
    
    """
    valid_user_input = validate_book_title(book_title) and validate_book_author(book_author) and validate_book_isbn(book_isbn) and validate_book_count(book_count)

    if valid_user_input:

        """
            Library validation
                -> check if the book already exists
                    -> increase book count if so
                -> Otherwise add new book
                We are assuming 1 to 1 match b/w title and isbn, so only search for title
        """

        book_exists = book_exists_in_library(book_title)

        # Add book to library
        if book_exists: library[book_title]["book_count"] += 1
        else: library[book_title] = {"book author" : book_author, "book isbn" : book_isbn, "book count" : book_count, "checkout number": 0}
        # return True for success
        return True
    # return False as book failed to be entered
    return False


# Return a list of search results that match (including substrings) book title, author, or isbn
def search_library(search_term):
    search_results = []
    search_term = search_term.title()
    # Iterate through the library to find matches
    for book_title, book_data in library.items():
        if search_term in book_title:
            search_results.append(book_title)
        elif search_term in book_data["book author"]:
            search_results.append(book_title)
        elif search_term in book_data["book isbn"]:
            search_results.append(book_title)

    
    return search_results

def print_library():
    print("The following books are contained in the library")   
    print("{:<50} {:<30} {:<20} {:<15} {:<15}".format("Title", "Author", "ISBN", "Copies Available", "Copies checked out"))
    print("-" * 130)  # Separator line

    for book_title, book_data in library.items():
        print("{:<50} {:<30} {:<20} {:<15} {:<15}".format(book_title, book_data["book author"], book_data["book isbn"], book_data["book count"], book_data["checkout number"]))

    return True


def print_loans_data():
    print("The following entries are contained in the Loan list")
    print("{:<20} {:<30} {:<20} {:<15} {:<15}".format("Full Name", "Title", "Loan Date", "Due Date", "Loan Duration (days)"))
    print("-" * 110)  # Separator line

    for person, loan_list in loan.items():
        for loan_data in loan_list:
            print("{:<20} {:<30} {:<20} {:<15} {:<15}".format(person, loan_data["book title"], loan_data["loan date"].strftime("%b %d %Y"), loan_data["due date"].strftime("%b %d %Y"), loan_data["loan duration"]))

    return True

"""
Error codes:
 "1" -> multiple books match search
"2" -> No book found
"3" -> No copies available
"4" -> Invalid name
"5" -> invalid duration
"""
def loan_book_from_library(book_title, loan_fullname, loan_duration):
    book_title = book_title.title()
    loan_fullname = loan_fullname.title()
    # Verify only 1 match for search
    book_exists = search_library(book_title)
    if book_exists == [] or len(book_exists) >1 :
        # multiple matches found
        return "1"
    
    # Verify book exists in library
    elif not book_exists_in_library(book_title):
        return "2"

    # Verify there are available copies in Library
    elif number_of_books_available(book_title) < 1:
        return "3"
    
    # Verify loaner entered their name
    elif not validate_fullname(loan_fullname):
        return "4"

    # Verify loan duration
    elif not validate_loan_duration(loan_duration):
        return "5"

    loan_checkout_start_date = dt.datetime.now()
    loan_checkout_end_date = loan_checkout_start_date + dt.timedelta(days=int(loan_duration))
    # If loaner already has a book loaned out, append the new book to the tuple 
    if loan_fullname in loan:
        loan[loan_fullname].append({"book title" : book_title, "loan date" : loan_checkout_start_date, "due date" : loan_checkout_end_date, "loan duration" : loan_duration})

    else:

        # Add loan to the loan dictionary. Set as a dictionary of a tuple of dictionaries
        loan[loan_fullname] = ([{"book title" : book_title, "loan date" : loan_checkout_start_date, "due date" : loan_checkout_end_date, "loan duration" : loan_duration}])

    # Decrement books available by 1
    library[book_title]["book count"] -= 1

    # increment checked out books by one
    library[book_title]["checkout number"] += 1

    return True

def check_loan_status(name):
    name = name.title()
    # Validate name has loaned a book
    name_exists = name_exists_in_loan(name)
    if (name_exists):
        return loan[name]
    return False

# Assume name exists in loan dict
def print_loan_status(name):
    name = name.title()
    print("The following entries are contained in the Loan list")
    print("{:<20} {:<30} {:<20} {:<15} {:<15}".format("Full Name", "Title", "Loan Date", "Due Date", "Loan Duration (days)"))
    print("-" * 110)  # Separator line
    for loan_list in loan.values():
        for loan_data in loan_list:
            print("{:<20} {:<30} {:<20} {:<15} {:<15}".format(name, loan_data["book title"], loan_data["loan date"].strftime("%b %d %Y"), loan_data["due date"].strftime("%b %d %Y"), loan_data["loan duration"]))


    return False


# Return loaned book
def return_loaned_book(loaner_name, loaner_book):
    # First check if loaner name and the book match the loan dict
    if check_loan_status(loaner_name):
        loans = loan[loaner_name]
        for loan_data in loans:
            if loaner_book == loan_data["book title"]:
                loans.remove(loan_data)
                library[loaner_book]["book count"] += 1
                library[loaner_book]["checkout number"] -= 1


"""

Validation Functions

"""
# Validate book title is a string and alphanumerical
def validate_book_title(book_title): return book_title.replace(" ", "").replace("-", "").replace("'", "").replace(",", "").replace(".", "").isalnum()

# Validate book author is a string and only alphabetiocal characters
def validate_book_author(book_author): return book_author.replace(" ", "").replace("-", "").replace("'", "").isalpha()

# Validate book isbn is only comprised of dashes and numbers
def validate_book_isbn(book_isbn): return book_isbn.replace("-", "").isnumeric()


# Validate book count is a positive int
def validate_book_count(book_count): 
    try:
        count = int(book_count)
        return count > 0
    except: return False


def validate_fullname(name):
    return name.replace(" ", "").replace("-", "").replace("'", "").isalpha()


def validate_loan_duration(duration):
    try:
        duration = int(duration)
        return 0 < duration <= 14
    except: return False




"""

End Validation Functions

"""



def book_exists_in_library(book): return library.get(book, False)

def number_of_books_available(book): return library[book].get("book count")

def name_exists_in_loan(name):
    name = name.title()
    return loan.get(name, False)


def library_main_menu():
    while True:
        print("Select options below")
        print("1. Add a book")
        print("2. Search for a book: ")
        print("3. Display all books in the Library: ")
        print("4. Loan a book")
        print("5. Check loan status")
        print("6. Display all Loan data")
        print("7. Return loaned book")
        print("q. Quit program")
        user_input = input("Enter selection: ")
  

        if user_input == "1":
            book_title = input("Please enter the title of the book: ")
            book_author = input("Please enter the author of the book ")
            book_isbn = input("Please enter the book ISBN: ")
            book_count = input("Please enter thenumber of copies: ")
            if not add_book_to_library(book_title, book_author, book_isbn, book_count):
                print("Error! You have entered an invalid book. Please try again")
            else: print(f"Sucess! You have added {book_title} to the Library")

        # Search the library
        elif user_input == "2":
            search_book = input("Search for a book: ")
            search_results = search_library(search_book)
            if not search_results: print(f"No books in the library match your search term: {search_book}")
            else: print(f"The following books match your search: {search_results}")

    
        # Print the Library
        elif user_input == "3":
            print_library()


        # loan a book
        elif user_input == "4":
            # Gather required information to checkout a book
            book = input("Enter the book title you would like to loan: ")
            name = input("Enter you full name: ")
            legnth = input("Enter how long you would like to loan the book [days]: ")
            loan_success = loan_book_from_library(book, name, legnth)
            if loan_success == True:
                print(f"You successfully loaned {book} from the library for {legnth} days")
            elif loan_success == "1":
                print(f"Error, multiple books have been found for your search {book}. Please try again")
            elif loan_success == "2":
                print(f"Error. Your search for {book} is not found in the Library")
            elif loan_success == "3":
                print(f"There are no copies available for {book}. Please try again tomorrow.")
            elif loan_success == "4":
                print("You entered an invalid name. Please try again")
            elif loan_success == "5":
                print("You entered an invalid loan duration. Please be sure to select a value between 1-14 days")
            else: print("Error. Something went wrong. Please try again later")


        # Display Loan dict for a person
        elif user_input == "5":
            name = input("Enter your name: ")
            name_exists = name_exists_in_loan(name)
            if name_exists: print_loan_status(name)
            else: print("Error. You do not have any books loaned or you have misspelled your name. Please try again")
       
        # Display Loan dict
        elif user_input == "6": print_loans_data()
        
        elif user_input == "7":
            loaner_name = input("Please enter your name: ").title()
            loaner_book = input("Please enter the book you are returning: ").title()
            return_loaned_book(loaner_name, loaner_book)

        elif user_input == "q":
            sys.exit()
