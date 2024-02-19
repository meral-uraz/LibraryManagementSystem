# Library Management System
This is a simple Library Management System implemented in Python.

## Features

- List Books: Displays the list of books available in the library.
- Add Book: Allows the user to add a new book to the library.
- Remove Book: Allows the user to remove a book from the library.
- Exit: Exits the program.

## Usage

1. Run the program by executing the LibraryManagementSystem.py file.
2. Follow the on-screen menu to perform desired actions:
   - To list books, enter 1.
   - To add a book, enter 2 and follow the prompts.
   - To remove a book, enter 3 and provide the title of the book to remove.
   - To quit the program, enter 4.
3. Follow the prompts and instructions provided by the program.

## Notes

- The program stores book information in a file named books.txt.
- Each line in the books.txt file represents a single book, with the following format:
  book_title,book_author,release_date,num_pages
- Make sure to properly enter the information when adding or removing books.
- The program ensures that invalid choices are handled gracefully.
