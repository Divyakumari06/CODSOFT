class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, due_date=None):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {
            'name': task_name,
            'due_date': due_date,
            'completed': False
        }
        print(f"Task '{task_name}' added with ID {task_id}")

    def view_tasks(self):
        for task_id, task_info in self.tasks.items():
            print(f"{task_id}. {task_info['name']} ({task_info['due_date']}) - {task_info['completed']}")

    def update_task(self, task_id, updates):
        if task_id in self.tasks:
            for key, value in updates.items():
                self.tasks[task_id][key] = value
            print(f"Task {task_id} updated")
        else:
            print(f"Task ID {task_id} not found")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['completed'] = True
            print(f"Task {task_id} marked as completed")
        else:
            print(f"Task ID {task_id} not found")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task {task_id} deleted")
        else:
            print(f"Task ID {task_id} not found")


if __name__ == "__main__":
    my_list = ToDoList()
    my_list.add_task("Buy groceries", "2023-03-12")
    my_list.add_task("Submit report")
    my_list.view_tasks()
    my_list.update_task(1, {'due_date': '2023-03-14'})
    my_list.complete_task(1)
    my_list.delete_task(2)
    my_list.view_tasks()