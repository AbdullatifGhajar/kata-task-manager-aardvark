import pytest

from src.task import Task

def test_task():
    task = Task("Test task")
    assert task.name == "Test task"
    assert task.is_done == False