from TaskFlow.models import Task


class TaskNotFoundError(Exception):
    """Raised when no task has the given id."""


class TaskManager:
    def __init__(self, tasks: list[Task] | None = None):
        self.tasks = tasks if tasks is not None else []

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Title cannot be empty.")
        next_id = max((t.id for t in self.tasks), default=0) + 1
        task = Task(next_id, title)
        self.tasks.append(task)
        return task

    def find(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(f"No task with id {task_id}.")

    def complete(self, task_id: int) -> Task:
        task = self.find(task_id)
        task.mark_done()
        return task

    def delete(self, task_id: int) -> Task:
        task = self.find(task_id)
        self.tasks.remove(task)
        return task

    def list_tasks(self) -> list[Task]:
        return list(self.tasks)