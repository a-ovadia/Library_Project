from Books import Book
from BookCollection import BookCollection
from Library import Library
from LibraryManager import LibraryManager
from Person import Person

# List of fake books
books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "123456789"),
    Book("1984", "George Orwell", "987654321"),
    Book("To Kill a Mockingbird", "Harper Lee", "111222333"),
    Book("Pride and Prejudice", "Jane Austen", "444555666"),
    Book("The Catcher in the Rye", "J.D. Salinger", "777888999"),
    Book("The Hobbit", "J.R.R. Tolkien", "101112131"),
    Book("Fahrenheit 451", "Ray Bradbury", "141516171"),
    Book("Moby Dick", "Herman Melville", "181920212"),
    Book("War and Peace", "Leo Tolstoy", "232425262"),
    Book("The Odyssey", "Homer", "272829303")
]


book_collections = [
    BookCollection(books[0], total_count=5),
    BookCollection(books[1], total_count=3),
    BookCollection(books[2], total_count=4),
    BookCollection(books[3], total_count=6),
    BookCollection(books[4], total_count=2),
    BookCollection(books[5], total_count=8),
    BookCollection(books[6], total_count=7),
    BookCollection(books[7], total_count=1),
    BookCollection(books[8], total_count=9),
    BookCollection(books[9], total_count=10)
]

library = Library(book_collections)
library_manager = LibraryManager(library)
library_manager.main_menu()