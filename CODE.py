import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display menu
def show_menu():
    print("\n------- TO-DO LIST -------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    print("--------------------------")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            if not tasks:
                print("No tasks to delete.")
                continue

            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if _name_ == "_main_":
    main()
