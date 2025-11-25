import pytest
from app import add_task, list_tasks, update_task, delete_task, clear_tasks

@pytest.fixture(autouse=True)
def setup_and_teardown():
    clear_tasks()
    yield
    clear_tasks()

def test_add_task():
    task = add_task("Buy groceries")
    assert task["title"] == "Buy groceries"
    assert task["id"] == 1
    assert task["completed"] is False
    assert len(list_tasks()) == 1

def test_add_task_empty_title():
    with pytest.raises(ValueError, match="Title cannot be empty"):
        add_task("")
    with pytest.raises(ValueError, match="Title cannot be empty"):
        add_task("   ")

def test_list_tasks():
    add_task("Task 1")
    add_task("Task 2")
    tasks = list_tasks()
    assert len(tasks) == 2
    assert tasks[0]["title"] == "Task 1"
    assert tasks[1]["title"] == "Task 2"

def test_update_task():
    task = add_task("Original Title")
    updated_task = update_task(task["id"], title="New Title", completed=True)
    assert updated_task["title"] == "New Title"
    assert updated_task["completed"] is True
    
    tasks = list_tasks()
    assert tasks[0]["title"] == "New Title"
    assert tasks[0]["completed"] is True

def test_update_task_empty_title():
    task = add_task("Task")
    with pytest.raises(ValueError, match="Title cannot be empty"):
        update_task(task["id"], title="   ")

def test_update_nonexistent_task():
    result = update_task(999, title="New")
    assert result is None

def test_delete_task():
    task = add_task("To be deleted")
    assert delete_task(task["id"]) is True
    assert len(list_tasks()) == 0

def test_delete_nonexistent_task():
    assert delete_task(999) is False

