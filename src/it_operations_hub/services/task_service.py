from it_operations_hub.database.db import get_connection

def create_task(title, description='', priority='Medium', due_date=None):
    """Create a new task in the database."""
    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO tasks (title, description, priority, due_date)
            VALUES (?, ?, ?, ?)
            """,
            (title.strip(), description, priority, due_date)
        )
        return cursor.lastrowid

def get_all_tasks():
    """Retrieve all tasks from the database."""
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM tasks ORDER BY created_at DESC, id DESC").fetchall()
        return [dict(row) for row in rows]

def update_task_status(task_id, status):
    """Update the status of a task."""
    valid_statuses = ['Open', 'In Progress', 'Completed']
    if status not in valid_statuses:
        raise ValueError("Invalid task status.")

    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (status, task_id)
        )
        return cursor.rowcount > 0

def delete_task(task_id):
    """Delete a task from the database."""
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        return cursor.rowcount > 0