import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    schema_file = Path(__file__).resolve().parent / "schema.sql"
    with open(schema_file, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


def add_task(title, description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (title, description),
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id


def list_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, completed FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def complete_task(task_id):
    """Mark a task as completed"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?",
        (task_id,),
    )
    conn.commit()
    affected = cur.rowcount
    conn.close()
    return affected > 0  # True if item was updated


def delete_task(task_id):
    """Delete a task by ID"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,),
    )
    conn.commit()
    conn.close()
    return cur.rowcount > 0  # True if deleted
