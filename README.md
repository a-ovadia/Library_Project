# Library Management System

Welcome to the Library Management System project. This repository contains a Python-based application designed to manage library operations such as book loans, returns, and catalog management. The system also manages library users and their library cards.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- **Book Management**: Add, remove, and search for books in the library catalog.
- **User Management**: Register new users, issue library cards, and manage user information.
- **Loan Management**: Check out and return books, track loaned books, and manage overdue books.
- **Search Functionality**: Search books by title, author, ISBN, publication date, genre, and publisher.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/a-ovadia/Library_Project.git
    cd Library_Project/Class%20Src
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

1. **Run the application:**
  (TODO main file)
    ```bash
    python main.py
    ```

2. **Follow the on-screen instructions to navigate through the menu options:**

   - View all books in the library
   - Search the library
   - Check if a book is available
   - Loan a book
   - Check loan status
   - View overdue books

## Project Structure

```plaintext
.
├── Books.py
├── BookCollection.py
├── Library.py
├── LibraryCard.py
├── LibraryManager.py
├── Person.py
├── PrintOut.py
└── main.py
```
- Books.py: Contains the Book class that defines book attributes.
- BookCollection.py: Manages the collection of books in the library.
- Library.py: Handles library operations and book management.
- LibraryCard.py: Manages library card details.
- LibraryManager.py: Provides an interface between the library and user input, handling the main application logic.
- Person.py: Defines the Person class for library users.
- PrintOut.py: Contains functions for formatted print statements.
- main.py: (TODO) Entry point for the application.

