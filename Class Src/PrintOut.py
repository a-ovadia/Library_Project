import LibraryManager
import Person

def print_loaned_books(user_list):
    for entry in user_list:
        print(f"Name: {entry.get_name()}")
        print("Loaned Books:")
        
        for item in entry.get_loaned_books():
            print(f"  - {item.get_title()}")
        
        print("-" * 40)