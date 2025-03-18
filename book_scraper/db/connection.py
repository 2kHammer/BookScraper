import os
from pymongo import MongoClient

def get_db():
    con_string = os.getenv("CONNECTION_STRING")
    db_name = os.getenv("DB_NAME")
    client = MongoClient(con_string)
    db = client[db_name]
    return db, client

def close_db(client):
    client.close()