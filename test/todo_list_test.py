import pytest

from src.todo_list import TodoList
from src.task import Task


def test_init():
    todo_list = TodoList()
    
    assert todo_list
    
def test_has_tasks_as_dict():
    todo_list = TodoList()
    
    assert todo_list.tasks == {}
    
def test_add_task():
    todo_list = TodoList()
    
    task_description = "Do the dishes"
    todo_list.add_task(task_description)
    
    assert todo_list.tasks[1]
    assert todo_list.tasks[1].name == task_description
    
def test_set_add_tasks():
    todo_list = TodoList()
    
    task_description1 = "Do the dishes"
    todo_list.add_task(task_description1)
    
    task_description2 = "Do the laundry"
    todo_list.add_task(task_description2)
    
    assert len(todo_list.tasks) == 2
    assert todo_list.tasks[1].name == task_description1
    assert todo_list.tasks[2].name == task_description2