
def main():
    manager = TaskManager("tasks.json")

    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            try:
                task = manager.add_task(title)
                print(f"Task added successfully! ID: {task['id']}")
            except ValueError as e:
                print(e)

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{task['id']}. {task['title']} - {status}")

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                task = manager.complete_task(task_id)

                if task:
                    print("Task marked as completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                print("Task deleted successfully!")
            except ValueError as e:
                print(e)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
