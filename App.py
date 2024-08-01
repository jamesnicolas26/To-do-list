#class

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task {task} added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task {task} removed.")
        else:
            print(f"Task {task} not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                print(f"- {task}")

todo_list = TodoList()
while True:
    print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        todo_list.add_task(task)
    elif choice == "2":
        task = input("Enter your task to remove: ")
        todo_list.remove_task(task)
    elif choice == "3":
        todo_list.view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")