import sys

if len(sys.argv) < 2:
    print("Please give a command: ")
else:
    command = sys.argv[1]
    
    if command == 'add':
        if len(sys.argv) < 3:
            print("Please provide a task description:")
        else:
            description = sys.argv[2]
            print("Adding task:", description)
            
    elif command == 'list':
        print("Listing tasks..")
        
    elif command == 'delete':
        print("Deleting task..")
        
    else:
        print("Unknown command.")
        

