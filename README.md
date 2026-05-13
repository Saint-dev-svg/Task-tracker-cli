# Task Tracker CLI
A simple command-line task tracker application built with Python.
This project allows users to add, update, delete, and manage tasks directly from the terminal using a JSON file for storage.

## Features
- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as in-progress
- Mark tasks as done
- List all tasks
- Filter tasks by status
- Persistent JSON storage
- Command-line interface

## Technologies Used
- Python
- JSON
- Git
- GitHub

## Installation

1. Clone the repository

```bash
git clone https://github.com/Saint-dev-svg/task-tracker-cli.git
```

2. Navigate into the project folder

```bash
cd task-tracker-cli
```

3. Run the application

```bash
python main.py
```

## Usage

### Add a Task

```bash
python main.py add "Buy groceries"
```

### List All Tasks

```bash
python main.py list
```

### List Done Tasks

```bash
python main.py list done
```

### Update a Task

```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a Task

```bash
python main.py delete 1
```

### Mark Task as In Progress

```bash
python main.py mark-in-progress 1
```

### Mark Task as Done

```bash
python main.py mark-done 1
```

## Project Structure

task-tracker-cli/
│
├── main.py
├── tasks.json
├── README.md
└── .gitignore

## What I Learned

Through this project I learned:
- Command-line application development
- JSON file handling
- CRUD operations
- Git and GitHub workflows
- Error handling and validation
- Python file handling
- Software engineering fundamentals

## Future Improvements

- Add due dates
- Add task priorities
- Add colored terminal output
- Add search functionality
- Store tasks in a database
