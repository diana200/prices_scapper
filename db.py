
import pymongo
import config


client = pymongo.MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]

products = db["products"]
offer_history = db["offer_history"]
alerts = db["alerts"]
