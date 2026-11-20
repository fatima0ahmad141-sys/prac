from library import LibraryError
from storage import Storage

MENU = ("\n1 Add book · 2 Add member · 3 List books · 4 List members"
        " · 5 Borrow · 6 Return · 7 Quit")


def read_int(prompt):
    """Ask for a number; return an int or None if the input isn't a number."""
    try:
        return int(input(prompt))
    except ValueError:
        print("Please type a number.")
        return None


def print_all(items, empty_message):
    if not items:
        print(empty_message)
    for item in items:
        print(item)


def main():
    storage = Storage()
    library = storage.load()

    while True:
        print(MENU)
        choice = input("> ").strip()
        try:
            if choice == "1":
                book = library.add_book(input("Title: "), input("Author: "))
                print(f"Added book {book.id}.")
            elif choice == "2":
                name = input("Name: ")
                premium = input("Premium? (y/n): ").strip().lower() == "y"
                member = library.add_member(name, premium)
                print(f"Added member {member}.")
            elif choice == "3":
                print_all(library.books, "No books yet.")
            elif choice == "4":
                print_all(library.members, "No members yet.")
            elif choice in ("5", "6"):
                book_id = read_int("Book id: ")
                if book_id is None:
                    continue
                if choice == "5":
                    book = library.borrow_book(book_id, input("Member name: ").strip())
                    print(f"{book.borrowed_by} borrowed '{book.title}'.")
                else:
                    book = library.return_book(book_id)
                    print(f"'{book.title}' returned.")
            elif choice == "7":
                storage.save(library)
                print("Bye!")
                break
            else:
                print("Choose 1–7.")
        except (LibraryError, ValueError) as e:
            print(e)
        else:
            storage.save(library)


if __name__ == "__main__":
    main()
