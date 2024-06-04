import Library
import random
import datetime as dt

# This is an internal testing program to test the functionality of the Library program

def populate_test_library(num_books=150):
    """Adds a specified number of test books to the library."""
    titles = [
        "The Hitchhiker's Guide to the Galaxy",
        "Pride and Prejudice",
        "1984",
        "To Kill a Mockingbird",
        "The Lord of the Rings",
        "The Great Gatsby",
        "One Hundred Years of Solitude",
        "The Catcher in the Rye",
        "Moby Dick",
        "Crime and Punishment",
        "War and Peace",
        "The Odyssey",
        "Alice's Adventures in Wonderland",
        "The Adventures of Sherlock Holmes",
        "Don Quixote",
        "The Handmaid's Tale",
        "Brave New World",
        "The Metamorphosis",
        "Dune",
        "The Book Thief",
        "The Adventures of Huckleberry Finn",
        "Les Misérables",
        "The Count of Monte Cristo",
        "Jane Eyre",
        "Frankenstein",
        "The Adventures of Tom Sawyer",
        "The Three Musketeers",
        "Treasure Island",
        "Dracula",
        "The Time Machine",
        "The War of the Worlds",
        "The Invisible Man",
        "The Strange Case of Dr. Jekyll and Mr. Hyde",
        "The Wind in the Willows",
        "The Secret Garden",
        "The Call of the Wild",
        "Peter Pan",
        "Anne of Green Gables",
        "The Lion, the Witch and the Wardrobe",
        "The Hobbit",
        "The Little Prince",
        "The Alchemist",
        "The Da Vinci Code",
        "The Kite Runner",
        "A Thousand Splendid Suns",
        "Life of Pi"
    ]

    authors = [
        "Douglas Adams",
        "Jane Austen",
        "George Orwell",
        "Harper Lee",
        "J.R.R. Tolkien",
        "F. Scott Fitzgerald",
        "Gabriel Garcia Marquez",
        "J.D. Salinger",
        "Herman Melville",
        "Fyodor Dostoevsky",
        "Leo Tolstoy",
        "Homer",
        "Lewis Carroll",
        "Arthur Conan Doyle",
        "Miguel de Cervantes",
        "Margaret Atwood",
        "Aldous Huxley",
        "Franz Kafka",
        "Frank Herbert",
        "Markus Zusak",
        "Mark Twain",
        "Victor Hugo",
        "Alexandre Dumas",
        "Charlotte Brontë",
        "Mary Shelley",
        "Mark Twain",
        "Alexandre Dumas",
        "Robert Louis Stevenson",
        "Bram Stoker",
        "H.G. Wells",
        "H.G. Wells",
        "H.G. Wells",
        "Robert Louis Stevenson",
        "Kenneth Grahame",
        "Frances Hodgson Burnett",
        "Jack London",
        "J.M. Barrie",
        "L.M. Montgomery",
        "C.S. Lewis",
        "J.R.R. Tolkien",
        "Antoine de Saint-Exupéry",
        "Paulo Coelho",
        "Dan Brown",
        "Khaled Hosseini",
        "Khaled Hosseini",
        "Yann Martel",
    ]
    print(f"Len titles is {len(titles)}")
    for i in range(len(titles)):
        title = titles[i]
        author = authors[i] # ensure correct author for each title
        isbn = f"978-0-{random.randint(100000000, 999999999)}"  # Generate random ISBN
        count = random.randint(1, 10)  # Random number of copies (1-5)
        Library.add_book_to_library(title, author, isbn, count)

# Call the function to populate your library with 20 test books
populate_test_library()


print(Library.return_total_book_count())
print(Library.return_unique_books())

Library.checkout_book("Adam o", "life of pi", dt.datetime.now, dt.timedelta(200))
print(f"the value is {Library.has_checked_out_book("Adam o", "life oF Pi")}")
print(Library.borrowers)
Library.return_book_to_library("Adam o", "Life of Pi")

# Library.library_main_menu()



