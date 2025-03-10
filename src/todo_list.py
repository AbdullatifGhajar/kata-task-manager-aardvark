from src.task import Task

class TodoList:
    def __init__(self):
        self.tasks = {}
        self.counter = 1
        
    def add_task(self, description:str):
        self.tasks[self.counter] = Task(description)
        self.counter += 1

    def set_done(self, id:int):
        self.tasks[id].is_done = True

    def set_todo(self, id:int):
        self.tasks[id].is_done = False  

    def remove_task(self, id:int):
        del self.tasks[id]