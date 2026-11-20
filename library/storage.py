import json
from dataclasses import asdict
from pathlib import Path

from library import Library
from models import Book, Member, PremiumMember


class Storage:
    def __init__(self, path: str = "library.json"):
        self.path = Path(path)
        self.backup_path = Path("library.backup.json")

    def save(self, library: Library) -> None:
        data = {
            "books": [asdict(book) for book in library.books],
            "members": [
                {"name": m.name, "premium": isinstance(m, PremiumMember)}
                for m in library.members
            ],
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self) -> Library:
        if not self.path.exists():
            return Library()
        try:
            with open(self.path, encoding="utf-8") as f:
                data = json.load(f)
            books = [Book(**item) for item in data["books"]]
            members = [
                PremiumMember(m["name"]) if m["premium"] else Member(m["name"])
                for m in data["members"]
            ]
            return Library(books, members)
        except (json.JSONDecodeError, KeyError, TypeError):
            self.path.replace(self.backup_path)
            return Library()
