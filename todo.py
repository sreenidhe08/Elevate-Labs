# todo.py

def display_menu():
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("=================================")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✔️ Done" if task["done"] else "❌ Pending"
            print(f"{i}. {task['title']} [{status}]")


def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully!")


def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter task number to mark as done: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Deleted task: {removed['title']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
