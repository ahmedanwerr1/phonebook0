import os

def load_todo_list():
    with open("todo_list.txt", "r") as f:
        tasks = f.readlines()
    tasks = [task.strip() for task in tasks]
    tasks = [task for task in tasks if task]
    return tasks

def save_todo_list(tasks):
    with open("todo_list.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def create_todo_list():
    name = input("Enter a name for the new to-do list: ")
    tasks = []
    save_todo_list(tasks)
    print(f"To-do list '{name}' created.")

def delete_task(tasks):
    index = int(input("Enter the index of the task to delete: "))
    if index < 0 or index >= len(tasks):
        print("Invalid index.")
    else:
        task = tasks.pop(index)
        print(f"Task '{task}' deleted.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i}. {task}")

    tasks = load_todo_list()

while True:
    print("Menu:")
    print("1. Add a task to the current to-do list.")
    print("2. Create a new to-do list.")
    print("3. Delete a task from the current to-do list.")
    print("4. List all tasks in the current to-do list.")
    print("5. Quit the program.")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        create_todo_list()
        tasks = []
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        list_tasks(tasks)
    elif choice == "5":
        save_todo_list(tasks)
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")