from src.todo_list import TodoList

class UserInterface:
    def __init__(self):
        self.todo_list = TodoList()

    def print_todo_list(self):
        print("No tasks yet!")