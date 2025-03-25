
def display_menu():
    print("\nTo-Do List Options:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for idx, (task, done) in enumerate(tasks, 1):
            status = "✔" if done else "✗"
            print(f"{idx}. [{status}] {task}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append((task, False))
    print(f"Task '{task}' added!")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = (tasks[task_num - 1][0], True)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task[0]}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_done(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                print("Exiting... Have a productive day!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
