import os

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self, file_name="library.txt"):
        self.file_name = file_name
        self.books = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r", encoding="utf-8") as f:
                for line in f:
                    if "=" in line:
                        title, author, status = line.strip().split("=")
                        borrowed = (status == "True")
                        self.books.append(Book(title, author, borrowed))

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            for b in self.books:
                f.write(f"{b.title}={b.author}={b.is_borrowed}\n")

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save_data()
        print(f"'{title}' has been added to the library.")

    def delete_book(self, title):
        target_book = None
        for b in self.books:
            if b.title.lower() == title.lower():
                target_book = b
                break
        if not target_book:
            raise KeyError("The book to be deleted could not be found in the library.")
        self.books.remove(target_book)
        self.save_data()
        print(f"'{title}' has been deleted.")

    def borrow_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.is_borrowed:
                    raise ValueError("This book is already borrowed.")
                b.is_borrowed = True
                self.save_data()
                print(f"'{title}' has been borrowed.")
                return
        raise KeyError("The book to be borrowed could not be found.")

    def return_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                if not b.is_borrowed:
                    raise ValueError("This book is already in the library, not borrowed.")
                b.is_borrowed = False
                self.save_data()
                print(f"'{title}' has been returned.")
                return
        raise KeyError("The book to be returned does not belong to this library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        print("\n--- Book List ---")
        for b in self.books:
            status = "Borrowed" if b.is_borrowed else "Available"
            print(f"Book: {b.title} - Author: {b.author} [{status}]")

management = Library()

while True:
    print("\n1. Add Book")
    print("2. Delete Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. List Books")
    print("6. Exit")
    choice = input("Your choice = ").strip()
    try:
        if choice == "1":
            t = input("Book Title = ").strip()
            a = input("Author Name = ").strip()
            management.add_book(t, a)
        elif choice == "2":
            t = input("Book Title to Delete = ").strip()
            management.delete_book(t)
        elif choice == "3":
            t = input("Book Title to Borrow = ").strip()
            management.borrow_book(t)
        elif choice == "4":
            t = input("Book Title to Return = ").strip()
            management.return_book(t)
        elif choice == "5":
            management.list_books()
        elif choice == "6":
            print("Closing...")
            break
        else:
            print("Invalid choice! Please use options between 1 and 6.")
    except (KeyError, ValueError) as error:
        print(f"An error occurred = {error}")