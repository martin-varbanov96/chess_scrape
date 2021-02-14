# load_data.py
from PersonalVariables import personal_variables as pv
import pymongo

class DataLoader:
    def __init__(self):
        self.mongo_client = pymongo.MongoClient(pv.mongo_connection)
        self.db = self.mongo_client[pv.cloud_mongo_db]

    def mongo_many_insert_to_collection(self, collection, docs_list):
        assert(type(docs_list) == list)
        assert(type(collection) == str)
        col = self.db[collection]
        status = col.insert_many(docs_list)

        if(status == []):
            print("Nothing was inserted")
