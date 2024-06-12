import LibraryManager
import Person
from datetime import datetime

def print_loaned_books(user_list):
    for entry in user_list:
        print(f"\n{'='*20}\nName: {entry.get_name()}\n{'='*20}")
        print("Loaned Books:")
        
        for item in entry.get_loaned_books():
            print(f"  - {item.get_title()}")
        
        print("\n" + "-" * 40)

def print_loans_for_person(person: Person):
    print(f"\n{'='*20}\nName: {person.get_name()}\nLibrary Card ID: {person.get_library_card()}\n{'='*20}")
    print("Loaned Books:")
    for book in person.get_loaned_books():
        print(f"  - {book.get_title()}")
    print("\n" + "-" * 40)

def print_all_books(library_manager):  # type: (LibraryManager.LibraryManager) -> None
    print("\nAll Books in the Library:\n" + "="*40)
    for book_collection in library_manager.get_library().get_book_collection():
        book = book_collection.get_book()
        print(f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_isbn()}")
        print("-" * 40)

def print_available_books(library_manager):  # type: (LibraryManager.LibraryManager) -> None
    print("\nAvailable Books:\n" + "="*40)
    for book_collection in library_manager.get_library().get_book_collection():
        if book_collection.number_available > 0:
            book = book_collection.get_book()
            print(f"Title: {book.get_title()}\nAuthor: {book.get_author()}\nISBN: {book.get_isbn()}")
            print("-" * 40)

def print_person_list(library_manager):  # type: (LibraryManager.LibraryManager) -> None
    print("\nRegistered Persons:\n" + "="*40)
    for person in library_manager.get_person():
        print(f"Name: {person.get_name()}\nEmail: {person.get_email()}\nPhone: {person.get_phone()}")
        print("-" * 40)

def print_overdue_books(library_manager):  # type: (LibraryManager.LibraryManager) -> None
    print("\nOverdue Books:\n" + "="*40)
    for person in library_manager.get_person():
        for book in person.get_loaned_books():
            if book.get_due_date() and datetime.datetime.now() > book.get_due_date():
                print(f"Name: {person.get_name()}\nBook Title: {book.get_title()}\nDue Date: {book.get_due_date()}")
                print("-" * 40)