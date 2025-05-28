# Articles-Challenge

A Python application modeling relationships between Authors, Articles, and Magazines.

## Setup

1. Initialize the database:
   ```bash
   python scripts/setup_db.py
   ```

2. Install dependencies:
   ```bash
   pip install pipenv
   pipenv install --dev
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Try example queries:
   ```bash
   python scripts/run_queries.py
   ```

## Project Structure

- `lib/`: Core application code
  - `models/`: Database models
  - `db/`: Database connection and schema
- `tests/`: Test cases
- `scripts/`: Utility scripts

## Models

- `Author`: Writers who create articles
- `Magazine`: Publications containing articles
- `Article`: Individual pieces of content