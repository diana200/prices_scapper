import dotenv
import os
from pymongo import MongoClient

dotenv.load_dotenv()

MONGO_URI = dotenv.get_key(".env","MONGO_URI")
DB_NAME = dotenv.get_key(".env","DB_NAME")
API_KEY = os.getenv("PRICES_API_KEY")

# print(API_KEY)

# if not MONGO_URI:
#     print("env data was not loaded!")
#     MONGO_URI = "mongodb://localhost:27017"
#
# if not DB_NAME:
#     DB_NAME = "price_scaper"


client = MongoClient(MONGO_URI)
db = client[str(DB_NAME)]

products = db["products"]
offer_history = db["offer_history"]
alerts = db["alerts"]
#
#
# ALERT_THRESHOLD_DEFAULT = 100.0  # exemplu
