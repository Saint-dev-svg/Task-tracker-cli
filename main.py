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

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
        
    return None

def get_current_time():
    return datetime.now().replace(microsecond=0).isoformat()

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
            
            current_time = get_current_time()
            
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
                print("____________________________________")
                print(f"ID: {task['id']}")
                print(f"Description: {task['description']}")
                print(f"Status: {task['status']}")
                print(f"Created at: {task['created At']}")
                print(f"Updated At: {task['Updated At']}")
                print("____________________________________")
               
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Please provide task ID and new description.")

        else:
            try:
                task_id = int(sys.argv[2])

            except ValueError:
                print("Task ID must be a number.")

            else:
                new_description = sys.argv[3]
                tasks = load_tasks()
                task = find_task_by_id(tasks, task_id)
                
                if task:
                    task['description'] = new_description
                    task['Updated At'] = get_current_time()
                    save_tasks(tasks)
                    print(f"Task {task_id} updated successfully.")

                else:
                    print("Task not found.")
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Please provide a task ID:")
        
        else:
            try:
                task_id = int(sys.argv[2])
            
            except ValueError:
                print("Task ID must be a number.")
                
            else:
                tasks = load_tasks()    
                updated_tasks = []
                task_found = False
                
                for task in tasks:
                    if task["id"] == task_id:
                        task_found = True
                    
                    else:
                        updated_tasks.append(task)
                
                if task_found:
                    save_tasks(updated_tasks)
                    print(f"Task {task_id} deleted successfully.")
                
                else:
                    print("Task not found.")
    
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Please provide a task ID:")
        
        else:
            try:
                task_id = int(sys.argv[2])
                
            except ValueError:
                print("Task ID must be a number.")
                
            else:
                tasks = load_tasks()
                task = find_task_by_id(tasks, task_id)
                
                if task:
                    task['status'] = "in-progress"
                    task['Updated At'] = get_current_time()
                    save_tasks(tasks)
                    print(f"Task {task_id} marked as in progress.")
                        
                else:
                    print("task not found.")
    
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Please provide a task ID:")
        
        else:
            try:
                task_id = int(sys.argv[2])
                
            except ValueError:
                print("Task ID must be a number.")
                
            else:
                tasks = load_tasks()
                task = find_task_by_id(tasks, task_id)
                
                if task:
                    task['status'] = "done"
                    task['Updated At'] = get_current_time()
                    save_tasks(tasks)
                    print(f"Task {task_id} marked as done.")
                        
                else:
                    print("task not found.")
    
    else:
        print("Unknown command.")