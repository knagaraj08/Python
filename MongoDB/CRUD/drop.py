
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Library_info"]

collections = db["Books"]


# this will drop the collection that was created
# collections.drop() 

print(db.list_collection_names())