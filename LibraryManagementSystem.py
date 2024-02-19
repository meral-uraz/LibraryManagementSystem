class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        
        if not lines :
            print("\nThere are no books in the library.")
        else :
            for line in lines:
                book_info = line.strip().split(',')
                print("\nBook:", book_info[0])
                print("Author:", book_info[1])
                print("Release Date:", book_info[2])
                print("Number of Pages:", book_info[3])
                print()

    def add_book(self):
        book_title = input("\nEnter book title: ")
        book_author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        pages_num = input("Enter number of pages: ")
        book_info = f"{book_title},{book_author},{release_date},{pages_num}\n"
        self.file.write(book_info)
        print("\nBook added successfully.")

    def remove_book(self):
        book_title = input("\nEnter book title to remove: ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        new_lines = []
        for line in lines:
            if book_title not in line:
                new_lines.append(line)
        self.file.seek(0)
        self.file.truncate()
        for line in new_lines:
            self.file.write(line)
        print("\nBook removed successfully.")

lib = Library()

while True:
    print("\n *** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        print("\nExiting the program...")
        break
    else:
        print("\nInvalid choice. Please enter 1, 2, 3 or 4.")

