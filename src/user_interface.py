from src.todo_list import TodoList

class UserInterface:
    def __init__(self):
        self.todo_list = TodoList()

    def print_todo_list(self):
        if self.todo_list.tasks == {}:
            print("No tasks yet!")
        else:
            for id, task in self.todo_list.tasks.items():
                print(f"{id} {'[x]' if task.is_done else '[ ]'} {task.description}")
                
    def apply_input(self, input: str):
        command, arguments = input.split(" ", 1)
        match command:
            case "+":
                task_description = arguments
                self.todo_list.add_task(task_description)
            case "-":
                task_id = int(arguments)
                self.todo_list.remove_task(task_id)
            
        
      
      