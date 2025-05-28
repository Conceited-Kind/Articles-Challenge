from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.seed import seed_database
from scripts.setup_db import setup_database as setup_db
from lib.db.connection import get_connection

setup_db()
seed_database()

# Check database contents
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM authors")
print("Authors:", [dict(row) for row in cursor.fetchall()])
cursor.execute("SELECT * FROM magazines")
print("Magazines:", [dict(row) for row in cursor.fetchall()])
cursor.execute("SELECT * FROM articles")
print("Articles:", [dict(row) for row in cursor.fetchall()])
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tables:", [row['name'] for row in cursor.fetchall()])
conn.close()

author = Author.find_by_id(1)
print("Author.find_by_id(1):", author.name if author else None)
magazine = Magazine.find_by_id(1)
print("Magazine.find_by_id(1):", magazine.name if magazine else None)
top_mag = Magazine.top_publisher()
print("Top Publisher:", top_mag.name if top_mag else None)