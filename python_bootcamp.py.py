class Library:
    def __init__(self, menu):
        # Initialize the Library object with the given menu (file).
        self.menu_name = menu
        # Open the menu file in 'a+' mode, allowing both reading and appending.
        self.menu_file = open(menu, 'a+')

    def __del__(self):
        # Destructor method to close the menu file when the object is deleted.
        self.menu_file.close()

    def list_books(self):
        # Method to list all the books in the menu file.
        self.menu_file.seek(0)
        # Move the file pointer to the beginning of the file.
        lines = self.menu_file.readlines()
        # Read all lines from the file.
        if lines:
            # If there are lines in the file:
            print("- List of Books -\n")
            # Print a header for the list of books.
            for line in lines:
                # Iterate through each line in the file.
                title, author, releaseYear, numOfPage = line.strip().split(',')
                # Split the line into its components (title, author, release year, number of pages).
                print("Title: ", title)
                print("Author: ", author)
                print("Release Year: ", releaseYear)
                print("Number of Pages: ", numOfPage)
                print()
                # Print the book details.
        else:
            # If there are no lines in the file:
            print("Please add a book!")
            # Print a message indicating that there are no books in the library.
        return True

    def add_book(self):
        # Method to add a new book to the menu file.
        title = input("Enter book title: ")
        author = input("Enter name of book author: ")
        releaseYear = input("Enter release year: ")
        numOfPage = input("Enter number of pages: ")

        self.menu_file.write(f"{title},{author},{releaseYear},{numOfPage}\n")
        print("Book added successfully.")
        return True

    def remove_book(self):
        # Method to remove a book from the menu file (placeholder implementation).
        title = input("Enter the title of the book to remove: ")
        return True

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
        if lib.remove_book():
            break
        
    elif choice == '4':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice. Please try again.")