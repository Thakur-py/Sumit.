#Project Title: To-Do List Application

import os

# Global variables
tasks = []
task_id_counter = 1
filename = "tasks.txt"

# Function to load tasks from a text file
def load_tasks():
    global task_id_counter
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                task_info = line.strip().split("|")
                if len(task_info) == 3:
                    task_id, task_title, task_description = task_info
                    task_id = int(task_id)
                    task_id_counter = max(task_id, task_id_counter) + 1
                    tasks.append({
                        "id": task_id,
                        "title": task_title,
                        "description": task_description,
                        "completed": False
                    })

# Function to save tasks to a text file
def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['title']}|{task['description']}|{task['completed']}\n")

# Function to display the to-do list
def show_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("To-Do List:")
        for task in tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

# Function to add a task to the list
def add_task(title, description):
    global task_id_counter
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    task_id_counter += 1
    print(f"Task '{title}' added.")

# Function to mark a task as complete or uncompleted
def mark_task(task_id, status):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = status
            print(f"Task ID: {task_id} marked as {'Completed' if status else 'Not Completed'}.")
            return
    print("Task not found.")

# Function to delete a task from the list
def delete_task(task_id):
    global task_id_counter
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task ID: {task_id} deleted.")
            return
    print("Task not found.")

# Main function
def main():
    load_tasks()
    
    while True:
        print("\nOptions:")
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed/Not Completed")
        print("4. Delete Task")
        print("5. Save and Quit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            add_task(title, description)
        elif choice == '3':
            task_id = int(input("Enter the task ID: "))
            status = input("Mark as completed (C) or not completed (NC): ").lower()
            if status == "c":
                mark_task(task_id, True)
            elif status == "nc":
                mark_task(task_id, False)
            else:
                print("Invalid input. Use 'C' or 'NC'.")
        elif choice == '4':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
