class Book:
    def __init__(self, title, author, price):
        # Information about each book
        self.title = title
        self.author = author
        self.price = price
        self.available = True  # Every new book is available initially

    def borrow(self):
        # Borrow the book only if it's available
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        # Return the book only if it was borrowed
        if not self.available:
            self.available = True
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' is already in the library.")

    def display(self):
        status = "Available" if self.available else "Borrowed"

        print("---------------")
        print(f"Title     : {self.title}")
        print(f"Author    : {self.author}")
        print(f"Price     : ₹{self.price}")
        print(f"Status    : {status}")
        print("---------------")


class Library:
    def __init__(self):
        # A library stores many Book objects
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nLibrary Books:\n")
        for book in self.books:
            book.display()


# --------------------------
# Create Book Objects
# --------------------------

book1 = Book("Naruto", "Masashi Kishimoto", 500)
book2 = Book("One Piece", "Eiichiro Oda", 650)
book3 = Book("Dragon Ball", "Akira Toriyama", 450)
book4 = Book("Attack on Titan", "Hajime Isayama", 700)

# --------------------------
# Create Library
# --------------------------

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

# Display all books
library.display_books()

# Borrow a book
book2.borrow()

# Display again
library.display_books()

# Return the book
book2.return_book()

# Display again
library.display_books()