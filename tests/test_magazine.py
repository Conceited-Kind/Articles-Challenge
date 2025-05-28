import pytest
from lib.models.magazine import Magazine
from lib.db.seed import seed_database
from scripts.setup_db import setup_database as setup_db

@pytest.fixture
def setup_database():
    setup_db()
    seed_database()
    yield

def test_magazine_creation(setup_database):
    magazine = Magazine("Test Mag", "Test Category")
    assert magazine.id is not None
    assert magazine.name == "Test Mag"
    assert magazine.category == "Test Category"

def test_magazine_articles(setup_database):
    magazine = Magazine.find_by_id(1)
    assert magazine is not None, "Magazine with ID 1 not found in database"
    articles = magazine.articles()
    assert len(articles) > 0, "No articles found for magazine ID 1"
    assert articles[0]["magazine_id"] == 1

def test_top_publisher(setup_database):
    top_mag = Magazine.top_publisher()
    assert top_mag is not None, "No top publisher found"