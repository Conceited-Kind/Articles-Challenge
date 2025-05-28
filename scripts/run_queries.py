from lib.db.connection import get_connection

def run_example_queries():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Get all articles by a specific author
    cursor.execute("SELECT * FROM articles WHERE author_id = ?", (1,))
    print("Articles by author 1:", [dict(row) for row in cursor.fetchall()])

    # 2. Magazines an author has contributed to
    cursor.execute("""
        SELECT DISTINCT m.* FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        WHERE a.author_id = ?
    """, (1,))
    print("Magazines for author 1:", [dict(row) for row in cursor.fetchall()])

    # 3. Authors for a specific magazine
    cursor.execute("""
        SELECT DISTINCT a.* FROM authors a
        JOIN articles art ON a.id = art.author_id
        WHERE art.magazine_id = ?
    """, (1,))
    print("Authors for magazine 1:", [dict(row) for row in cursor.fetchall()])

    # 4. Magazines with at least 2 different authors
    cursor.execute("""
        SELECT m.*, COUNT(DISTINCT a.author_id) as author_count
        FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        HAVING author_count >= 2
    """)
    print("Magazines with 2+ authors:", [dict(row) for row in cursor.fetchall()])

    # 5. Count articles per magazine
    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count
        FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    print("Article count per magazine:", [dict(row) for row in cursor.fetchall()])

    # 6. Author with the most articles
    cursor.execute("""
        SELECT a.*, COUNT(art.id) as article_count
        FROM authors a
        JOIN articles art ON a.id = art.author_id
        GROUP BY a.id
        ORDER BY article_count DESC
        LIMIT 1
    """)
    print("Top author:", dict(cursor.fetchone()))

    conn.close()

if __name__ == "__main__":
    run_example_queries()