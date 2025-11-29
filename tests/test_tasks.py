import os
from database.db import add_task, list_tasks, init_db, DB_PATH

def setup_module(module):
    # delete old test DB
    if DB_PATH.exists():
        os.remove(DB_PATH)
    init_db()

def test_add_task():
    task_id = add_task("Test task", "Testing db insert")
    assert isinstance(task_id, int)

def test_list_tasks():
    add_task("Another task", "Test retrieval")
    tasks = list_tasks()
    assert len(tasks) >= 1
    assert "title" in tasks[0]
