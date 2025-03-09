# Simple To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet! Add some.\n")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):  
            print(f"{i + 1}. {tasks[i]}")

    print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid number!\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
