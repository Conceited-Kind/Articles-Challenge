from lib.db.connection import get_connection

class Author:
    def __init__(self, name, id=None):
        self._id = id
        self._name = None
        self.name = name
        if id is None:
            self.save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self._id is None:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (self._name,))
                self._id = cursor.lastrowid
            else:
                cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self._name, self._id))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        print(f"Author.find_by_id({id}): {dict(row) if row else None}")
        conn.close()
        return cls(row['name'], row['id']) if row else None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def add_article(self, magazine, title):
        conn = get_connection()
        try:
            conn.execute("BEGIN TRANSACTION")
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                (title, self._id, magazine.id)
            )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self._id,))
        rows = cursor.fetchall()
        conn.close()
        return [row['category'] for row in rows]