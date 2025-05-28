import pytest
from lib.models.article import Article
from lib.db.seed import seed_database
from scripts.setup_db import setup_database as setup_db  # Renamed to avoid naming conflict

@pytest.fixture
def setup_database():
    setup_db()  # Call the function from scripts/setup_db.py
    seed_database()
    yield  # Ensure database is available during tests
    # Optional: Clean up database after tests if needed

def test_article_creation(setup_database):
    article = Article("Test Article", 1, 1)
    assert article.id is not None
    assert article.title == "Test Article"
    assert article.author_id == 1
    assert article.magazine_id == 1