from config.mongo_config import get_db

def run():
    db = get_db()
    db.users.insert_many([
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"}
    ])
    db.products.insert_many([
        {"name": "Laptop", "price": 1500},
        {"name": "Mouse", "price": 25}
    ])
    print("Initial data inserted")