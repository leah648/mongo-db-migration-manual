# check_db.py
from config.mongo_config import get_db
from pymongo import MongoClient
from pprint import pprint

def main():
    client = MongoClient("mongodb://localhost:27017")  # או מה שיש לך ב-MONGO_URI
    print("Databases:", client.list_database_names())

    db = get_db()
    print("\nCollections in DB:", db.name)
    for collection_name in db.list_collection_names():
        print(f"\nDocuments in collection '{collection_name}':")
        for doc in db[collection_name].find():
            pprint(doc)

if __name__ == "__main__":
    main()