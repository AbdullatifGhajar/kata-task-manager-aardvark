import pytest

from src.user_interface import UserInterface
from src.todo_list import TodoList

# TODO: ask teacher if we need ui in the name

def test_init():
    user_interface = UserInterface()

    assert type(user_interface.todo_list) == TodoList
    