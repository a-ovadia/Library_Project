# TODO - Refactor Library program into a class[s]

# Assume one-to-one relationship b/w title and isbn


import datetime as dt

library = {}
borrowers = {}


def add_book_to_library(title, author, isbn, count=1):
    # Need function to determine if book already exists (search function)
    existing_book = helper_search_if_book_exists(title.title())
    if existing_book:
        library[title.title()]["number_available"] += count
    else:
        library[title.title()] = {"author": author.title(), "isbn": isbn, "number_available": count}


# Search for a book in the Library
# Search by by title, author, or isbn. Searches for partial matches
def search_for_a_book(search):
    search = search.lower()
    search_results = []
    for title, book_data in library.items():
        if (search in title.lower()) or \
           (search in book_data.get("author", "").lower().split()) or \
           (search in book_data.get("isbn", "").split()):
            search_results.append(title)
    
    return search_results    

# return key of valid book
# Search through title or isbn match only
# Assume 1 to 1 relationship b/w title and isbn
def helper_search_if_book_exists(search_title):
    return library.get(search_title, False)


def get_user_search_for_book():
    return input("Search for a book: ")


# Assumes boot_title exists in dictionary
def helper_search_number_of_books(book_title):
    return library[book_title]["number_available"] > 0


def helper_checkout_book(book_title):
    # Check if book exists
    if helper_search_if_book_exists(book_title.title()):

        # Check number_available to make sure a book is available
        if helper_search_number_of_books(book_title.title()):
            # for now, just update library -> future work on logging checkouts in a dict
            library[book_title.title()]["number_available"] -= 1
        else:
            print("The book exists, but there are no copies left. Please try tomorrow to see if any copies have "
                  "been returned")
    else:
        print("No book exists by that title. Please check your spelling and try again")


# Assumes valid book and copies available
def checkout_book(name, title, time_borrowed, return_date, book_returned=False):
    record = borrowers.get(name, [])
    record.append({"title": title, "time_borrowed": time_borrowed, "return_date": return_date, "book_returned": book_returned})
    borrowers[name] = record
    helper_checkout_book(title)


def is_name_valid_in_borrow(name):
    check = borrowers.get(name, False)
    if check:
        return True
    return False

# Validate whether a particular user has checked out the specified book
def has_checked_out_book(name, book_title):
    # Return True or False
    return

# Overall status of a book -> how many copies available, how many are checked out, who has checked out
def check_book_status(book_title):

    return

# Return who has borrow the specified book
def get_borrower(book_title):
    borrowers_list = []
    for key, value in borrowers.items():
        for checkout in value:
            if checkout.get("title") == book_title:
                borrowers_list.append(borrowers_list.append(key))
    return borrowers_list

# Return list of loans for a specified user
def get_loans_for_user(name):
    return borrowers.get(name, [])

    return

def library_main_menu():
    while True:
        print("Select options below")
        print("1. Add a book")
        print("2. Search for a book")
        print("3. Show contents of library")
        print("4. Checkout a book")
        print("5. Check what books you have checked out")
        print("6. Quit program")
        user_input = input("Enter selection: ")
        if not user_input.isnumeric():
            print("You entered an incorrect value. Please try again\n")

        if user_input == "1":
            title = input("Please enter the title of the book: ")
            author = input("Please enter the author: ")
            isbn = input("Please enter the ISBN: ")
            number = int(input("Please enter the number of copies: "))

            # Need to work on input validation
            add_book_to_library(title, author, isbn, number)

        if user_input == "2":
            input_result = get_user_search_for_book().title()
            search_result = search_for_a_book(input_result)
            if search_result:
                print(f"Your search returned a total of {len(search_result)} results \n {search_result}")
            else:
                print("No books match your search\n")

        if user_input == "3":
            print(library)

        if user_input == "4":
            book_to_checkout = input("Please enter the book which you would like to checkout: ").title()
            if not helper_search_if_book_exists(book_to_checkout):
                print("The book you have searched for does not exist. Please try again")
            else:
                name = input("Enter your name: ").title()
                length = input("Enter how many days you would like to have this book: ")
                checkout_time = dt.datetime.now()
                return_date = checkout_time + dt.timedelta(days=int(length))
                checkout_book(name, book_to_checkout, checkout_time, return_date)

        if user_input == "5":
            name = input("Enter your name: ").title()
            # Validate name in borrowers dict

            books = get_loans_for_user(name)
            print(type(books))
            if not books:
                print("You currently do not have any books checked out")
                continue
            else: print(books)
        if user_input == "6":
            print(get_borrower("my book".title()))
           # return False


