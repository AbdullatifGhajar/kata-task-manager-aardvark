from src.todo_list import TodoList

class UserInterface:
    def __init__(self):
        self.todo_list = TodoList()

    def print_todo_list(self):
        if self.todo_list.tasks == {}:
            print("No tasks yet!")
        else:
            print("1 [ ] Do the dishes")