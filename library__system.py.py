import datetime

library = {
    "1001": {"title": "Harry Potter", "author": "J.K. Rowling", "issued": False, "issue_date": None},
    "1002": {"title": "The Hobbit", "author": "J.R.R. Tolkien", "issued": False, "issue_date": None},
    "1003": {"title": "1984", "author": "George Orwell", "issued": False, "issue_date": None},
}

def display_books():
    print("\n--- Library Books ---")
    for book_id, info in library.items():
        status = "Issued" if info["issued"] else "Available"
        print(f"ID: {book_id} | Title: {info['title']} | Author: {info['author']} | Status: {status}")
    print()

def add_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        print("Book ID already exists.")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    library[book_id] = {"title": title, "author": author, "issued": False, "issue_date": None}
    print(f"Book '{title}' added successfully!")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    if book_id not in library:
        print("Book not found.")
        return
    if library[book_id]["issued"]:
        print("Book already issued.")
        return

    roll_no = input("Enter Student Roll Number: ")
    issue_time = datetime.datetime.now()
    library[book_id]["issued"] = True
    library[book_id]["issue_date"] = issue_time

    print("\n=== Book Issue Pass Card ===")
    print(f"Book ID   : {book_id}")
    print(f"Title     : {library[book_id]['title']}")
    print(f"Author    : {library[book_id]['author']}")
    print(f"Issued To : Roll No. {roll_no}")
    print(f"Issue Date: {issue_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("============================\n")

    print(f"Book '{library[book_id]['title']}' issued successfully!")

def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id not in library:
        print("Book not found.")
        return
    if not library[book_id]["issued"]:
        print("This book was not issued.")
        return

    issue_date = library[book_id].get("issue_date")
    return_date = datetime.datetime.now()
    days_held = (return_date - issue_date).days
    fine = 0
    if days_held > 10:
        fine = 10

    library[book_id]["issued"] = False
    library[book_id]["issue_date"] = None

    print(f"\nBook '{library[book_id]['title']}' returned successfully!")
    print(f"Days Held: {days_held} days")
    if fine > 0:
        print(f"Late Return Fine: ₹{fine}")
    else:
        print("No late fee.\n")

def renew_book():
    book_id = input("Enter Book ID to renew: ")
    if book_id not in library:
        print("Book not found.")
        return
    if not library[book_id]["issued"]:
        print("Book is not currently issued.")
        return

    current_date = datetime.datetime.now()
    issue_date = library[book_id].get("issue_date")
    days_held = (current_date - issue_date).days
    fine = 0
    if days_held > 12:  # 10 days due + 2 days grace
        fine = 10

    library[book_id]["issue_date"] = current_date

    print(f"\nBook '{library[book_id]['title']}' renewed successfully.")
    print(f"Days Since Issue: {days_held} days")
    if fine > 0:
        print(f"Late Renewal Fine: ₹{fine}")
    else:
        print("No fine on renewal.\n")

def search_book():
    query = input("Enter Book ID or Title to search: ").lower()
    found = False

    print("\n--- Search Results ---")
    for book_id, info in library.items():
        if query == book_id or query in info['title'].lower():
            status = "Issued" if info["issued"] else "Available"
            print(f"ID: {book_id} | Title: {info['title']} | Author: {info['author']} | Status: {status}")
            found = True

    if not found:
        print("Book not found.")
    print()

def main():
    while True:
        print("\n=== Library Management System ===")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Renew Book")
        print("6. Search Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            renew_book()
        elif choice == '6':
            search_book()
        elif choice == '7':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
