from src.task import Task

class TodoList:
    def __init__(self):
        self.tasks = {}
        
    def add_task(self, description:str):
        self.tasks[1] = Task(description)