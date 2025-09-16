import os

# The name of the file where tasks will be stored
FILENAME = "tasks.txt"

def load_tasks():
    """Loads tasks from the text file."""
    if not os.path.exists(FILENAME):
        return []  # Return an empty list if the file doesn't exist
    
    tasks = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            # The format is "[status] description" e.g., "[x] Buy groceries"
            status_part = line.split('] ')[0] + ']'
            description = '] '.join(line.split('] ')[1:])
            
            completed = True if status_part == '[x]' else False
            tasks.append({'task': description, 'completed': completed})
    return tasks

def save_tasks(tasks):
    """Saves the list of tasks to the text file."""
    with open(FILENAME, 'w') as file:
        for task in tasks:
            status = '[x]' if task['completed'] else '[ ]'
            file.write(f"{status} {task['task']}\n")

def display_tasks(tasks):
    """Displays all the tasks to the user."""
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
    else:
        for i, task in enumerate(tasks, 1):
            status = '✅' if task['completed'] else '🔲'
            print(f"{i}. {status} {task['task']}")
    print("-----------------------\n")

def add_task(tasks):
    """Adds a new task to the list."""
    task_description = input("Enter the new task: ")
    if task_description:
        tasks.append({'task': task_description, 'completed': False})
        save_tasks(tasks)
        print(f"✅ Task '{task_description}' added successfully!")
    else:
        print("❌ Task description cannot be empty.")

def delete_task(tasks):
    """Deletes a task from the list."""
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed_task['task']}' was deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def mark_task_complete(tasks):
    """Marks a specific task as completed."""
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            save_tasks(tasks)
            print(f"🎉 Task '{tasks[task_num - 1]['task']}' marked as complete!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    """The main function to run the application loop."""
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            display_tasks(tasks)
            if tasks: delete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
            if tasks: mark_task_complete(tasks)
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select a number from 1 to 5.")

# Run the main program
if __name__ == "__main__":
    main()