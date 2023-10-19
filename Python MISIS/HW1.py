class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("Stack is empty")


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((task, priority))

    def remove_task(self, task):
        temp_stack = Stack()
        removed = False

        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] != task:
                temp_stack.push(current_task)
            else:
                removed = True

        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

        if not removed:
            raise Exception("Task not found")

    def remove_duplicates(self):
        temp_stack = Stack()
        unique_tasks = set()

        while not self.tasks.is_empty():
            current_task = self.tasks.pop()
            if current_task[0] not in unique_tasks:
                temp_stack.push(current_task)
                unique_tasks.add(current_task[0])

        while not temp_stack.is_empty():
            self.tasks.push(temp_stack.pop())

    def __str__(self):
        temp_stack = Stack()
        sorted_tasks = []

        while not self.tasks.is_empty():
            temp_stack.push(self.tasks.pop())

        while not temp_stack.is_empty():
            task = temp_stack.pop()
            sorted_tasks.append(task)
            self.tasks.push(task)

        sorted_tasks.sort(key=lambda x: x[1])

        return "\n".join([f"Task: {task[0]}, Priority: {task[1]}" for task in sorted_tasks])


# instance
task_manager = TaskManager()
task_manager.new_task("Task 1", 3)
task_manager.new_task("Task 2", 1)
task_manager.new_task("Task 4", 1)
task_manager.new_task("Task 3", 2)
task_manager.new_task("Task 3", 2)

print(task_manager, '\n')

task_manager.remove_task("Task 4")

print(task_manager, '\n')

task_manager.remove_duplicates()

print(task_manager)
