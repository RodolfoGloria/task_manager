import os
import database.db as db

def setup_function():
    """Reset the database before each test"""
    if os.path.exists(db.DB_PATH):
        os.remove(db.DB_PATH)
    db.init_db()

def test_add_and_list_tasks():
    task_id = db.add_task("Buy milk", "2 liters of whole milk")
    assert task_id is not None

    tasks = db.list_tasks()
    assert len(tasks) == 1

    t = tasks[0]
    assert t["title"] == "Buy milk"
    assert t["description"] == "2 liters of whole milk"
    assert t["completed"] == 0

def test_complete_task():
    task_id = db.add_task("Learn Linux", "Practice basic commands")
    ok = db.complete_task(task_id)
    assert ok is True

    tasks = db.list_tasks()
    assert tasks[0]["completed"] == 1

def test_delete_task():
    task_id = db.add_task("Temp", "Delete me")
    ok = db.delete_task(task_id)
    assert ok is True

    tasks = db.list_tasks()
    assert len(tasks) == 0
