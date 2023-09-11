# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to view all tasks in the to-do list
def view_tasks():
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("\nYour to-do list is empty.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main loop for the to-do list application
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
