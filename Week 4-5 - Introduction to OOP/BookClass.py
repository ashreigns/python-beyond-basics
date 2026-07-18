class Book:
    def __init__(self, title, author, pages, is_read):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

library = []

while True:
    print("\n1. Add Book")
    print("2. List Unread Books")
    print("3. Exit")
    choice = input("Your choice = ").strip()
    if choice == "1":
        title = input("Book Title = ").strip()
        author = input("Author Name = ").strip()
        pages = int(input("Page Count = "))
        answer = input("Is it read? (yes/no) = ").strip().lower()
        is_read = (answer == "yes")

        new_book = Book(title, author, pages, is_read)
        library.append(new_book)
        print("Book successfully added.")
    elif choice == "2":
        print("\nUnread Books")
        for b in library:
            if not b.is_read:
                print(f"Book Title = {b.title}, Author = {b.author}, ({b.pages} pages)")
    elif choice == "3":
        print("System closing.")
        break