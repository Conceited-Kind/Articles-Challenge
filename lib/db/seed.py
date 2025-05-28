import sqlite3
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from lib.db.connection import get_connection

def seed_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Verify tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('authors', 'magazines', 'articles')")
        tables = [row[0] for row in cursor.fetchall()]
        if not all(table in tables for table in ['authors', 'magazines', 'articles']):
            raise Exception("Required tables (authors, magazines, articles) not found in database")

        # Clear existing data
        cursor.execute("DELETE FROM articles")
        cursor.execute("DELETE FROM authors")
        cursor.execute("DELETE FROM magazines")
        cursor.execute("DELETE FROM sqlite_sequence")  # Reset AUTOINCREMENT
        print("Cleared tables: articles, authors, magazines, sqlite_sequence")

        # Seed authors
        authors = [
            ("Zain Santos",),
            ("Allan Smith",),
            ("Dwayne Johnson",)
        ]
        cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)
        print(f"Inserted {cursor.rowcount} authors")
        cursor.execute("SELECT id FROM authors")
        author_ids = [row[0] for row in cursor.fetchall()]

        # Seed magazines
        magazines = [
            ("Tech Weekly", "Technology"),
            ("Fashion Trends", "Fashion"),
            ("Health Digest", "Health")
        ]
        cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)
        print(f"Inserted {cursor.rowcount} magazines")
        cursor.execute("SELECT id FROM magazines")
        magazine_ids = [row[0] for row in cursor.fetchall()]

        # Seed articles with dynamic IDs
        articles = [
            ("Tech Trends 2025", author_ids[0], magazine_ids[0]),
            ("AI Revolution", author_ids[0], magazine_ids[0]),
            ("Summer Styles", author_ids[1], magazine_ids[1]),
            ("Healthy Eating", author_ids[2], magazine_ids[2]),
            ("Fitness Tips", author_ids[2], magazine_ids[2])
        ]
        cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)
        print(f"Inserted {cursor.rowcount} articles")

        conn.commit()
        print("Database seeded successfully")
    except Exception as e:
        conn.rollback()
        print(f"Seeding failed: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()