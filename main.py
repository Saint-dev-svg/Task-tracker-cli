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