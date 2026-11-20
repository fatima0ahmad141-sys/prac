from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    borrowed_by: str | None = None

    @property
    def is_borrowed(self) -> bool:
        return self.borrowed_by is not None

    def __str__(self) -> str:
        status = f"borrowed by {self.borrowed_by}" if self.is_borrowed else "available"
        return f"{self.id}. {self.title} — {self.author} ({status})"


class Member:
    max_books = 2

    def __init__(self, name: str):
        self.name = name

    def can_borrow(self, borrowed_count: int) -> bool:
        return borrowed_count < self.max_books

    def __str__(self) -> str:
        return f"{self.name} (up to {self.max_books} books)"


class PremiumMember(Member):
    max_books = 5

    def __str__(self) -> str:
        return f"{self.name} ⭐ premium (up to {self.max_books} books)"
