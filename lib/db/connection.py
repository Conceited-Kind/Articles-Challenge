import sqlite3

def get_connection():
    conn = sqlite3.connect('/home/allan/Phase3/Articles-Challenge/articles.db')
    conn.row_factory = sqlite3.Row
    return conn