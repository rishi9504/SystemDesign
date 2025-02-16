# Designing a Task Management System
# Requirements
# The task management system should allow users to create, update, and delete tasks.
# Each task should have a title, description, due date, priority, and status (e.g., pending, in progress, completed).
# Users should be able to assign tasks to other users and set reminders for tasks.
# The system should support searching and filtering tasks based on various criteria (e.g., priority, due date, assigned user).
# Users should be able to mark tasks as completed and view their task history.
# The system should handle concurrent access to tasks and ensure data consistency.
# The system should be extensible to accommodate future enhancements and new features.

class Task:
    def __init__(self, title, description, due_date, priority, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.assignee = None
        self.reminder = None

    def assign_to(self, user):
        self.assignee = user

    def set_reminder(self, reminder):
        self.reminder = reminder

    def mark_completed(self):
        self.status = 'completed'

    def get_history(self):
        return [self.title, self.description, self.due_date, self.priority, self.status, self.assignee, self.reminder]

    def __str__(self):
        return f"Task: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Priority: {self.priority}, Status: {self.status}"

class TaskManagementSystem:
    def __init__(self):
        self.tasks = {}

    def create_task(self, title, description, due_date, priority, status):
        task = Task(title, description, due_date, priority, status)
        self.tasks[task.title] = task
        return task

    def update_task(self, title, description, due_date, priority, status):
        if title in self.tasks:
            task = self.tasks[title]
            task.description = description
            task.due_date = due_date
            task.priority = priority
            task.status = status
            return task
        return None

    def delete_task(self, title):
        if title in self.tasks:
            del self.tasks[title]
            return True
        return False

    def search_tasks(self, criteria):
        results = []
        for task in self.tasks.values():
            if criteria in task.title or criteria in task.description or criteria in task.due_date or criteria in task.priority or criteria in task.status:
                results.append(task)
        return results

    def filter_tasks(self, criteria):
        results = []
        for task in self.tasks.values():
            if criteria in task.title or criteria in task.description or criteria in task.due_date or criteria in task.priority or criteria in task.status:
                results.append(task)
        return results

    def get_task_history(self, title):
        if title in self.tasks:
            return self.tasks[title].get_history()
        return None

    def mark_task_completed(self, title):
        if title in self.tasks:
            self.tasks[title].mark_completed()
            return True
        return False

    def assign_task(self, title, user):
        if title in self.tasks:
            self.tasks[title].assign_to(user)
            return True
        return False

    def set_task_reminder(self, title, reminder):
        if title in self.tasks:
            self.tasks[title].set_reminder(reminder)
            return True
        return False

    def __str__(self):
        return f"Task Management System with {len(self.tasks)} tasks"

# Usage
task_management_system = TaskManagementSystem()
task1 = task_management_system.create_task("Task 1", "Description 1", "2023-01-01", "High", "Pending")
task2 = task_management_system.create_task("Task 2", "Description 2", "2023-02-01", "Medium", "In Progress")


print(task1)
print(task2)

task_management_system.update_task("Task 1", "Updated Description 1", "2023-01-02", "Medium", "Completed")
print(task_management_system.get_task_history("Task 1"))

task_management_system.delete_task("Task 2")
print(task_management_system.tasks)

task_management_system.search_tasks("Description 1")
task_management_system.filter_tasks("Medium")