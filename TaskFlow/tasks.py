class TaskNotFoundError(Exception):
    """Raised when no task has the given id."""


def add_task(tasks, title):
    """Create a task and add it to the list."""
    title = title.strip()
    if not title:
        raise ValueError("Title cannot be empty.")
    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    return task


def find_task(tasks, task_id):
    """Return the task with this id, or raise TaskNotFoundError."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise TaskNotFoundError(f"No task with id {task_id}.")


def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    task["done"] = True
    return task


def delete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    tasks.remove(task)
    return task


def list_tasks(tasks):
    return list(tasks)