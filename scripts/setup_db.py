import sqlite3
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(script_dir, '../lib/db/schema.sql')
    with open(schema_path, 'r') as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()
    print("Database schema created successfully.")

if __name__ == "__main__":
    setup_database()