# -------- Book Class --------
class Book:
    # Constructor to store book details
    def __init__(self, book_id, title, copies):
        self.book_id = book_id
        self.title = title
        self.total_copies = copies
        self.available_copies = copies

    # Display book details
    def __str__(self):
        return f"{self.book_id} - {self.title} | Available: {self.available_copies}/{self.total_copies}"


# -------- Patron Class --------
class Patron:
    # Constructor to store patron details
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    # Display patron details
    def __str__(self):
        return f"{self.patron_id} - {self.name} | Borrowed: {self.borrowed_books}"


# -------- Library Class --------
class Library:

    # Constructor to create empty dictionaries
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book_id, title, copies):

        # Check if the book already exists
        if book_id in self.books:
            self.books[book_id].total_copies += copies
            self.books[book_id].available_copies += copies
            print("Book copies updated successfully.")

        # Otherwise add a new book
        else:
            self.books[book_id] = Book(book_id, title, copies)
            print("Book added successfully.")

    # Register a new patron
    def register_patron(self, patron_id, name):

        # Check if patron already exists
        if patron_id in self.patrons:
            print("Patron already registered.")

        # Register new patron
        else:
            self.patrons[patron_id] = Patron(patron_id, name)
            print("Patron registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):

        # Check whether patron exists
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        # Check whether book exists
        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        # Check if book is available
        if book.available_copies == 0:
            print("Book is not available.")

        # Check if patron already borrowed the same book
        elif book_id in patron.borrowed_books:
            print("Book already borrowed by this patron.")

        # Borrow the book
        else:
            book.available_copies -= 1
            patron.borrowed_books.append(book_id)
            print("Book borrowed successfully.")

    # Return a borrowed book
    def return_book(self, patron_id, book_id):

        # Check whether patron exists
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        # Check whether book exists
        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        # Check if patron has borrowed this book
        if book_id in patron.borrowed_books:
            patron.borrowed_books.remove(book_id)
            book.available_copies += 1
            print("Book returned successfully.")

        # If not borrowed
        else:
            print("This patron has not borrowed this book.")

    # Display all books
    def show_books(self):

        # Check if library has books
        if not self.books:
            print("No books available.")

        else:
            print("\nBooks in Library:")
            for book in self.books.values():
                print(book)

    # Display all registered patrons
    def show_patrons(self):

        # Check if any patron is registered
        if not self.patrons:
            print("No patrons registered.")

        else:
            print("\nRegistered Patrons:")
            for patron in self.patrons.values():
                print(patron)


# -------- Main Program --------

# Create Library Object
library = Library()

# Run the menu until user chooses Exit
while True:

    # Display Menu
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show All Patrons")
    print("7. Exit")

    # Take user's choice
    choice = int(input("Enter your choice: "))

    # Add Book
    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        copies = int(input("Enter Number of Copies: "))
        library.add_book(book_id, title, copies)

    # Register Patron
    elif choice == 2:
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        library.register_patron(patron_id, name)

    # Borrow Book
    elif choice == 3:
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.borrow_book(patron_id, book_id)

    # Return Book
    elif choice == 4:
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.return_book(patron_id, book_id)

    # Show all books
    elif choice == 5:
        library.show_books()

    # Show all patrons
    elif choice == 6:
        library.show_patrons()

    # Exit program
    elif choice == 7:
        print("Thank you for using the Library Management System.")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")