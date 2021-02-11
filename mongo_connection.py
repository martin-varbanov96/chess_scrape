# mongo_connection.py
from PersonalVariables import personal_variables
import pymongo

mongo_connection = f"mongodb+srv://{personal_variables.cloud_mongo_user}:{personal_variables.cloud_mongo_password}@cluster0.qgh9n.mongodb.net/{personal_variables.cloud_mongo_db}?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_connection)
db = client.test



