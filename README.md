# Running Diary

A terminal-based training diary for logging running sessions between 2026 and 2035.

## Learning objective 
This project implements a running training diary using custom dataclasses and hand-built linked lists (rather than Python's built-in list operations) to practice low-level data structure manipulation (sorted insertion, pointer-based deletion) alongside file persistence and modular program design.

## Features
- Training sessions modeled with `@dataclass`
- Sessions stored in a custom sorted linked list per month
- Add and delete sessions from the linked list
- Text-based UI to add, and delete sessions and view whole calendar (sessions added on a day is market with * on the calendar)
- Sessions saved to and loaded from files (JSON, one per month)
- Modular code structure
- Developed in small, descriptive commits

## Known limitations/choices
- The calendar view is a static, one-time printout (year/month entered manually via the menu) rather than an interactive, navigable view. It does not support arrow-key navigation between days/months. Sessions on a given day are marked with a simple `*` rather than a highlighted/bracketed selection.

## Running it
```python main.py```


