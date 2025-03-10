import pytest

from src.user_interface import UserInterface
from src.todo_list import TodoList

# TODO: ask teacher if we need ui in the name

def test_init():
    user_interface = UserInterface()

    assert type(user_interface.todo_list) == TodoList

def test_print_empty_todo_list(capfd):
    user_interface = UserInterface()

    user_interface.print_todo_list()
    
    out, err = capfd.readouterr()
    assert out == "No tasks yet!\n"

def test_print_todo_list_with_one_todo_item(capfd):
    user_interface = UserInterface()
    user_interface.todo_list.add_task("Do the dishes")

    user_interface.print_todo_list()
    
    out, err = capfd.readouterr()
    assert out == "1 [ ] Do the dishes\n"
    
def test_print_todo_list_with_one_done_item(capfd):
    user_interface = UserInterface()
    user_interface.todo_list.add_task("Do the dishes")
    user_interface.todo_list.set_done(1)

    user_interface.print_todo_list()
    
    out, err = capfd.readouterr()
    assert out == "1 [x] Do the dishes\n"
    
def test_apply_input_to_add_a_task():
    user_interface = UserInterface() 
    user_interface.apply_input("+ New Task")
    
    assert user_interface.todo_list.tasks[1].description == "New Task"
    
def test_apply_input_to_delet_a_task():
  user_interface = UserInterface()
  user_interface.apply_input("+ New Task")
  
  user_interface.apply_input("- 1")
    
  assert user_interface.todo_list.tasks == {}
  
  
def test_apply_input_to_edit_a_todo_task():
    user_interface = UserInterface()
    user_interface.apply_input("+ New Task")
        
    user_interface.apply_input.is_done("o 1")
        
    assert user_interface.todo_list.tasks[1].is_done == True
    

    