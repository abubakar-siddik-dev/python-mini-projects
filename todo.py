tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print("Task added!")

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid task number")


if name == "main":
    while True:
        print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            index = int(input("Enter task number: "))
            delete_task(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice")
