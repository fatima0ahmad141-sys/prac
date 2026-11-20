import json
from dataclasses import asdict
from pathlib import Path

from TaskFlow.models import Task


class Storage:
    def __init__(self, path: str = "tasks.json"):
        self.path = Path(path)
        self.backup_path = Path("tasks.backup.json")

    def save(self, tasks: list[Task]) -> None:
        data = [asdict(task) for task in tasks]
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self) -> list[Task]:
        if not self.path.exists():
            return []
        try:
            with open(self.path, encoding="utf-8") as f:
                data = json.load(f)
            return [Task(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            self.path.replace(self.backup_path)
            return []