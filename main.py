import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

        
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent = 4)
        
def generate_task_id(tasks):
    if not tasks:
        return 1
    return tasks[-1]["id"] +1

if len(sys.argv) < 2:
    print("Please enter a command:")
else:
    command = sys.argv[1]
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Please give a task description:")
        
        else:
            description = sys.argv[2]
            tasks = load_tasks()
            task_id = generate_task_id(tasks)
            
            current_time = datetime.now().isoformat()
            
            new_task = {
                "id" : task_id,
                "description" : description,
                "status" : "to-do",
                "created At" : current_time,
                "Updated At" : current_time
            }
            
            tasks.append(new_task)
            save_tasks(tasks)
            
            print("Task added successfully. ID:", task_id)
    
    elif command == 'list':
        tasks = load_tasks()
        
        if len(sys.argv) == 3:
            status_filter = sys.argv[2]
            filtered_tasks = []
            
            for task in tasks:
                if task["status"] == status_filter:
                    filtered_tasks.append(task)
            
            tasks = filtered_tasks
        
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print("______________")
                print(f"ID: {task['id']}")
                print(f"Description: {task['description']}")
                print(f"Status: {task['status']}")
                print(f"Created at: {task['created At']}")
                print(f"Updated At: {task['Updated At']}")
                
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Please provide task ID and new description:")
        else:
            try:
                task_id = int(sys.argv[2])
            except ValueError:
                print("Task ID must be a number.")
            else:
                new_description = sys.argv[3]
                tasks = load_tasks()
                task_found = False
                
                for task in tasks:
                    if task["id"] == task_id:
                        task["description"] == new_description
                        task["Updated At"] == datetime.now().isoformat()
                        task_found = True
                        break
                if task_found:
                    save_tasks(tasks)
                    print(f"Task {task_id} updated successfully.")
                else:
                    print("Task not found.")
        
    else:
        print("Unknown command.")