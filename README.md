MongoDB Migration Manual

Manual migration workflow for MongoDB using Python, inspired by SQL-based migration workflows. This project demonstrates how to create collections and insert initial data manually, suitable for learning or small projects.

Project Structure
mongo-db-migration-manual/
│
├─ migrations/          # Migration scripts
│   ├─ 001_create_collections.py
│   ├─ 002_insert_initial_data.py
│
├─ config/
│   └─ mongo_config.py  # MongoDB connection settings
│
├─ main.py              # Script to run migrations manually
├─ check_db.py          # Script to inspect DB content
└─ requirements.txt     # Python dependencies

Prerequisites

Python 3.9+
MongoDB server running locally or accessible remotely
pymongo library

Install dependencies:
pip install -r requirements.txt

Configuration
Edit config/mongo_config.py to configure your MongoDB connection:

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "manual-migrations-db"

from pymongo import MongoClient

def get_db():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db

MONGO_URI – MongoDB server URI
DB_NAME – Database name (created automatically if it doesn’t exist)

Creating a Migration

Create a new Python file in the migrations/ folder.
Define a run() function that applies the migration.
Name your file with a numeric prefix to maintain execution order, e.g., 003_add_new_collection.py.
Example:

def run():
    db = get_db()
    db.new_collection.insert_one({"key": "value"})
    print("Migration applied: new_collection")

Tip: Each migration should be idempotent – safe to run multiple times without creating duplicates or errors.

Running Migrations
Run all migrations manually:
python main.py

Migrations are executed in order based on filename.
Each migration prints a message when applied.

Checking Database Content

After running migrations, you can inspect the database with:
python check_db.py

Lists all databases
Lists all collections in the target database
Displays all documents in each collection
This is similar to SELECT * FROM ... in SQL.

Notes

This is a manual migration system, ideal for small projects or learning purposes.
For production, consider integrating with automated CI/CD workflows.
MongoDB automatically creates the database and collections when first inserting documents.

Example Output
Running migration: 001_create_collections.py
Collections created: users, products
Running migration: 002_insert_initial_data.py
Initial data inserted

Databases: ['admin', 'local', 'demo_db']
Collections in DB: demo_db
Documents in collection 'users':
{'_id': ObjectId('64f1a2b8...'), 'name': 'Alice', 'email': 'alice@example.com'}
{'_id': ObjectId('64f1a2b9...'), 'name': 'Bob', 'email': 'bob@example.com'}
Documents in collection 'products':
{'_id': ObjectId('64f1a2ba...'), 'name': 'Laptop', 'price': 1500}
{'_id': ObjectId('64f1a2bb...'), 'name': 'Mouse', 'price': 25}