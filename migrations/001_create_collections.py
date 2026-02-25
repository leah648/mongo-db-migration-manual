from config.mongo_config import get_db

def run():
    db = get_db()
    # יצירת collections
    if "users" not in db.list_collection_names():
        db.create_collection("users")
    if "products" not in db.list_collection_names():
        db.create_collection("products")
    print("Collections created: users, products")