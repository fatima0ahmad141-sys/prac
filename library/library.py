from models import Book, Member, PremiumMember


class LibraryError(Exception):
    """Base class for every library error."""


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookAlreadyBorrowedError(LibraryError):
    pass


class BookNotBorrowedError(LibraryError):
    pass


class BorrowLimitError(LibraryError):
    pass


class Library:
    def __init__(self, books: list[Book] | None = None,
                 members: list[Member] | None = None):
        self.books = books if books is not None else []
        self.members = members if members is not None else []

    def add_book(self, title: str, author: str) -> Book:
        title, author = title.strip(), author.strip()
        if not title or not author:
            raise ValueError("Title and author cannot be empty.")
        next_id = max((b.id for b in self.books), default=0) + 1
        book = Book(next_id, title, author)
        self.books.append(book)
        return book

    def add_member(self, name: str, premium: bool = False) -> Member:
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        if any(m.name == name for m in self.members):
            raise ValueError(f"Member '{name}' already exists.")
        member = PremiumMember(name) if premium else Member(name)
        self.members.append(member)
        return member

    def find_book(self, book_id: int) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book
        raise BookNotFoundError(f"No book with id {book_id}.")

    def find_member(self, name: str) -> Member:
        for member in self.members:
            if member.name == name:
                return member
        raise MemberNotFoundError(f"No member called '{name}'.")

    def books_of(self, member_name: str) -> list[Book]:
        return [b for b in self.books if b.borrowed_by == member_name]

    def borrow_book(self, book_id: int, member_name: str) -> Book:
        book = self.find_book(book_id)
        member = self.find_member(member_name)
        if book.is_borrowed:
            raise BookAlreadyBorrowedError(
                f"'{book.title}' is already borrowed by {book.borrowed_by}.")
        if not member.can_borrow(len(self.books_of(member.name))):
            raise BorrowLimitError(
                f"{member.name} can't borrow more than {member.max_books} books.")
        book.borrowed_by = member.name
        return book

    def return_book(self, book_id: int) -> Book:
        book = self.find_book(book_id)
        if not book.is_borrowed:
            raise BookNotBorrowedError(f"'{book.title}' is not borrowed.")
        book.borrowed_by = None
        return book
