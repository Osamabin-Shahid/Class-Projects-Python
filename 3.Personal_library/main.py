import json

class BookCollection:
    """A class to manage a collection of books, allowing user to store and organize their reading material."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        # Initialize an empty list to store the books
        self.book_list = []

        # Define the storage file where the book collection is saved
        self.storage_file = 'books_data.json'

        # Load existing book data from the file into the collection (if available)
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from a JSON file into memory.
        If the file does not exist or is corrupted, start with an empty collection."""
        try:
            # Attempt to open and load the existing book data from the JSON file
            with open(self.storage_file, 'r') as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file does not exist or contains invalid data, start with an empty list
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a JSON file for permanent storage."""
        # Open the file in write mode and save the current book collection
        with open(self.storage_file, 'w') as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""
        # Prompt the user for details about the new book
        book_title = input("Enter Book Title: ")
        book_author = input("Enter Book Author: ")
        publication_year = input("Enter Publication Year: ")
        book_genre = input("Enter Book Genre: ")

        # Ask the user whether they have read the book or not
        is_book_read = (input("Have you read this book? (yes/no): ").lower().strip() == 'yes')

        # Create a new book dictionary with the provided details
        new_book = {
            'title': book_title,
            'author': book_author,
            'publication_year': publication_year,
            'genre': book_genre,
            'read': is_book_read,
        }

        # Add the new book to the collection and save it to the file
        self.book_list.append(new_book)
        self.save_to_file()
        print(f'Book "{book_title}" added to the collection.')

    def delete_book(self):
        """Remove a book from the collection by its title."""
        # Prompt the user to input the title of the book they want to delete
        book_title = input("Enter the title of the book you want to delete: ")

        # Search for the book in the collection and remove it if found
        for book in self.book_list:
            if book['title'].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(f'Book "{book_title}" removed from the collection.')
                return
        # If no book with the given title is found, notify the user
        print(f'Book "{book_title}" not found in the collection.')

    def find_book(self):
        """Search for a book in the collection by title or author name."""
        # Prompt the user to choose how they want to search (by title or author)
        search_type = input("Search by:\n1. Title\n2. Author\nEnter the number of your choice: ")

        # Ask the user for the search query (either a title or author name)
        search_text = input("Enter the title or author of the book you want to find: ").lower()

        # Search for books that match the search query (either in the title or author)
        found_books = [
            book
            for book in self.book_list
            if search_text in book['title'].lower() or search_text in book['author'].lower()
        ]

        # If books are found, display their details
        if found_books:
            for index, book in enumerate(found_books, 1):
                read_status = 'read' if book['read'] else 'unread'
                print(f"{index}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")
        else:
            # If no books are found, notify the user
            print(f'No books found matching "{search_text}".')

    def update_book(self):
        """Modify the details of an existing book in the collection."""
        # Prompt the user for the title of the book they want to edit
        book_title = input("Enter the title of the book you want to edit: ")

        # Search for the book in the collection
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                # Display current values and ask the user for updated details (or leave blank to keep the current value)
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["publication_year"] = input(f"New year ({book['publication_year']}): ") or book["publication_year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (input("Have you read this book? (yes/no): ").strip().lower() == "yes")
                # Save the updated collection to the file
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        # If no book with the given title is found, notify the user
        print("Book not found!\n")

    def show_all_books(self):
        """Display all books in the collection with their details."""
        # If the collection is empty, notify the user
        if not self.book_list:
            print("Your collection is empty.\n")
            return

        # Display details of all books in the collection
        print("Your Book Collection:")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {reading_status}")
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        # Calculate the total number of books and how many have been read
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])

        # Calculate the completion rate as a percentage
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            # Display the main menu with options
            print("""📚 Welcome to your book collection manager!""")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            # Handle the user's choice
            if user_choice == '1':
                self.create_new_book()  # Add a new book
            elif user_choice == '2':
                self.delete_book()  # Remove an existing book
            elif user_choice == '3':
                self.find_book()  # Search for books
            elif user_choice == '4':
                self.update_book()  # Update book details
            elif user_choice == '5':
                self.show_all_books()  # View all books
            elif user_choice == '6':
                self.show_reading_progress()  # View reading progress
            elif user_choice == '7':
                self.save_to_file()  # Save the collection to the file before exiting
                print("Thank you for using the book collection manager. Goodbye!")
                break  # Exit the loop and end the program
            else:
                # If the user enters an invalid choice, prompt them again
                print("Invalid choice. Please choose a number between 1 and 7.")

if __name__ == '__main__':
    # Create an instance of the BookCollection class and start the application
    my_collection = BookCollection()
    my_collection.start_application()
