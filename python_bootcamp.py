class Library:
    def __init__(self, book):
        self.book_name = book
        self.book_file = open(book, 'a+')

    def __del__(self):
        self.book_file.close()

    def list_books(self):
        self.book_file.seek(0)
        lines = self.book_file.readlines()
        if lines:
            print("- List of Books -\n")
            for line in lines:
                title, author, releaseYear, numOfPage = line.strip().split(',')
                print("Title: ", title)
                print("Author: ", author)
                print("Release Year: ", releaseYear)
                print("Number of Pages: ", numOfPage)
                print()
        else:
            print("Please add a book!")
        return True

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter name of book author: ")
        releaseYear = input("Enter release year: ")
        numOfPage = input("Enter number of pages: ")

        self.book_file.write(f"{title},{author},{releaseYear},{numOfPage}\n")
        print("Book added successfully.")
        return True

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        lines = self.book_file.readlines()
        self.book_file.seek(0)
        self.book_file.truncate()

        for line in lines:
            words = line.strip().split(',')
            if words and words[0] != title:
                self.book_file.write(line)

lib = Library('books.txt')

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if lib.list_books():
            break
        
    elif choice == '2':
        if lib.add_book():
            break
        
    elif choice == '3':
        lib.remove_book()
        print("Book removed successfully.")
        break
        
    elif choice == '4':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice. Please try again.")