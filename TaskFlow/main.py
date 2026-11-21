from manager import TaskManager, TaskNotFoundError
from storage import Storage

MENU = "\n1 Add · 2 List · 3 Complete · 4 Delete · 5 Quit"


def read_task_id():
    """Ask for an id; return an int or None if the input isn't a number."""
    try:
        return int(input("Task id: "))
    except ValueError:
        print("Please type a number.")
        return None


def print_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for task in tasks:
        print(task)


def main():
    storage = Storage()
    manager = TaskManager(storage.load())

    while True:
        print(MENU)
        choice = input("> ").strip()

        if choice == "1":
            try:
                task = manager.add(input("Title: "))
                storage.save(manager.tasks)
                print(f"Added task {task.id}.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            print_tasks(manager.list_tasks())

        elif choice in ("3", "4"):
            task_id = read_task_id()
            if task_id is None:
                continue
            try:
                if choice == "3":
                    manager.complete(task_id)
                    print(f"Task {task_id} marked as done.")
                else:
                    manager.delete(task_id)
                    print(f"Task {task_id} deleted.")
                storage.save(manager.tasks)
            except TaskNotFoundError as e:
                print(e)

        elif choice == "5":
            storage.save(manager.tasks)
            print("Bye!")
            break

        else:
            print("Choose 1–5.")


if __name__ == "__main__":
    main()