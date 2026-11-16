import sqlite3
from pathlib import Path

# Store application data outside the source code folder
DATA_DIR = Path.home() / ".it_operations_personal_hub"
DB_PATH = DATA_DIR / "hub.db"

def get_connection():
    """Create and return a SQLite database connection."""
    # Ensure the data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Connect to the SQLite database
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row  # Enable named column access
    connection.execute("PRAGMA foreign_keys = ON")  # Enable foreign key support    

    return connection

def initialize_database():
    """Create the application's tables if they do not exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT NOT NULL DEFAULT 'Medium',
                status TEXT NOT NULL DEFAULT 'Open',
                due_date TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)

    print(f"Database initialized at {DB_PATH}")