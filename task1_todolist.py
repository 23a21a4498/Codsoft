tasks = []

def add_task():
    task = input("Enter Task: ")
    tasks.append(task)
    print("Task Added Successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No Tasks Available.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    if len(tasks) > 0:
        task_no = int(input("Enter Task Number to Update: "))
        if 1 <= task_no <= len(tasks):
            new_task = input("Enter New Task: ")
            tasks[task_no - 1] = new_task
            print("Task Updated Successfully!")
        else:
            print("Invalid Task Number.")

def delete_task():
    view_tasks()
    if len(tasks) > 0:
        task_no = int(input("Enter Task Number to Delete: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task Deleted Successfully!")
        else:
            print("Invalid Task Number.")

while True:
    print("\n*** TO-DO LIST APPLICATION ***")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice. Please Try Again.")