import LibraryManager
import Person

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