from src.task import Task

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.counter = 1
        
    def add_task(self, description:str):
        self.tasks[self.counter] = Task(description)
        self.counter += 1