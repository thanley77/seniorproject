import pymongo
import json

def import_to_mongodb(json_file, db_name, coll_name):
    # connect to the MongoDB client
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client[db_name]
    coll = db[coll_name]

    with open(json_file, 'r') as f:
        data = json.load(f)

    coll.insert_one(data)

# example usage
import_to_mongodb('output.json', 'database', 'collection')

