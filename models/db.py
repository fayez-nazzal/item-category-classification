from pymongo import MongoClient
import os

client = MongoClient(os.environ['MONGO_SRV'])
db = client[os.environ['DB_NAME']]
