# Falcons Training — Python Practice

Practice projects from the Falcons Full-Stack Bootcamp (Week 1).

## Projects

### TaskFlow
A command-line task manager. Tasks are saved to `tasks.json`, so they are still there after a restart.

- Add, list, complete and delete tasks
- Clear error messages for wrong input (letters instead of a number, unknown task id)
- Built with classes: `Task`, `TaskManager`, `Storage`

### Library
A command-line library system. Books and members are saved to `library.json`.

- Add books and members
- Borrow and return books
- A normal member can borrow up to 2 books, a premium member up to 5
- Built with classes: `Book`, `Member`, `PremiumMember`, `Library`, `Storage`

## Requirements

- Python 3.12 or newer
- No extra libraries needed

## How to run

Clone the repository:

```bash
git clone https://github.com/fatima0ahmad141-sys/prac.git
cd prac
```

Run TaskFlow (from the `prac` folder):

```bash
cd TaskFlow
python main.py
```

Run Library (from the `prac` folder):

```bash
cd library
python main.py
```

> On macOS, use `python3` instead of `python`.

## Project structure

```
prac/
├── TaskFlow/
│   ├── main.py       # menu, input and printing
│   ├── manager.py    # TaskManager: add, complete, delete, list, find
│   ├── models.py     # Task dataclass
│   ├── storage.py    # load and save tasks.json
│   └── tasks.py      # Day 2 version, written with functions
└── library/
    ├── main.py       # menu, input and printing
    ├── library.py    # Library: borrow and return rules
    ├── models.py     # Book, Member, PremiumMember
    └── storage.py    # load and save library.json
```

## Team

- [fatima0ahmad141-sys](https://github.com/fatima0ahmad141-sys)
- [Suhaib-Alkhaldi](https://github.com/Suhaib-Alkhaldi)
- [ShahedQatash](https://github.com/ShahedQatash)
