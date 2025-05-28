import pytest
from lib.models.author import Author
from lib.db.seed import seed_database
from scripts.setup_db import setup_database as setup_db

@pytest.fixture
def setup_database():
    setup_db()
    seed_database()
    yield

def test_author_creation(setup_database):
    author = Author("Test Author")
    assert author.id is not None
    assert author.name == "Test Author"

def test_author_articles(setup_database):
    author = Author.find_by_id(1)
    assert author is not None, "Author with ID 1 not found in database"
    articles = author.articles()
    assert len(articles) > 0, "No articles found for author ID 1"
    assert articles[0]["author_id"] == 1

def test_author_magazines(setup_database):
    author = Author.find_by_id(1)
    assert author is not None, "Author with ID 1 not found in database"
    magazines = author.magazines()
    assert len(magazines) > 0, "No magazines found for author ID 1"