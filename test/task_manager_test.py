
import pytest

from src.task_manager import TaskManager


def test_init():
    task_manager = TaskManager()
    
    assert task_manager.list == []
    
