tasks = []

# Load tasks from the text file
try:
    file = open("tasks.txt", "r")

    for line in file:
        tasks.append(line.strip())

    file.close()

except FileNotFoundError:
    print("No existing task file found. Starting a new list.")


# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")


# Function to remove a task
def remove_task():
    view_tasks()

    if len(tasks) > 0:
        task_number = int(input("Enter the task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")


# Function to view tasks
def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYOUR TO-DO LIST")

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


# Function to save tasks to a text file
def save_tasks():
    file = open("tasks.txt", "w")

    for task in tasks:
        file.write(task + "\n")

    file.close()


# Main program
while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        remove_task()

    elif choice == "3":
        view_tasks()

    elif choice == "4":
        save_tasks()
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
