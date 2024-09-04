# Question 2: Python Data Structure Challenges in Real-World Scenarios

# Task 1: Library System Enhancement

def add_new_book(library):
    try:
        title = input("Enter the title of the book: ").title()
        author = input("Enter the author of the book: ").title()
        new_book = (title, author)

        if new_book in library:
            print(f"{title} already exists in library.")
            return
        else:
            library.append(new_book)
            print(f"{title} has been added to library successfully.")
            return
    except Exception as e:
        print(f"An error {e} occured.")

def display_library_books(library):
    print("")
    print("Library")
    print("-------")
    for i, book in enumerate(library):
        print(f"Book {i + 1}: \n  Title: ", book[0], "  Author: ", book[1])
    if not book:
        print("No books were found.")

def main():
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

    while True:
        print("\n1. Add new book into library")
        print("2. display all books in library")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_book(library)
        elif choice == "2":
            display_library_books(library)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()