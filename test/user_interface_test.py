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
    