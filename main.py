

import json
from pathlib import Path


class TaskManager:
    def __init__(self, storage_file=None):
        self.storage_file = Path(storage_file) if storage_file else None
        self.tasks = []
        self.next_id = 1
        self._load()

    # Add a new task with validation
    def add_task(self, title):
        if not isinstance(title, str):
            raise TypeError("Task title must be a string.")

        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        title = title.strip()

        task = {
            "id": self.next_id,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        self._save()

        return task

    # Display all tasks
    def list_tasks(self):
        return self.tasks

    # Mark a task as completed
   
    def complete_task(self, task_id):
     for task in self.tasks:
        if task["id"] == task_id:
            if task["completed"]:
                raise ValueError("Task is already completed.")

            task["completed"] = True
            self._save()
            return task

    raise ValueError(f"No task found with ID {task_id}.")


    # Delete a task using its ID
    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self._save()
                return True

        raise ValueError(f"No task found with ID {task_id}.")

    # Load tasks from JSON file
    def _load(self):
        if self.storage_file and self.storage_file.exists():
            data = json.loads(self.storage_file.read_text())
            self.tasks = data["tasks"]
            self.next_id = data["next_id"]

    # Save tasks to JSON file
    def _save(self):
        if self.storage_file:
            data = {
                "tasks": self.tasks,
                "next_id": self.next_id
            }

            self.storage_file.write_text(
                json.dumps(data, indent=2)
            )


# Main console application
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
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")

                for task in tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(
                        f"{task['id']}. {task['title']} - {status}"
                    )

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
                print(f"Error: {e}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
