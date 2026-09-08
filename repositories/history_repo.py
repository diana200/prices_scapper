# from db import offer_history
import string

from db import offer_history

def add_history(entry):
    offer_history.insert_one({
        "offer_id": entry.offer_id,
        "product_id": entry.product_id,
        "seller": entry.seller,
        "price": entry.price,
        "available": entry.available,
        "timestamp": entry.timestamp
    })

def get_history(offer_id: string):
    return list(offer_history.find({"offer_id": offer_id}).sort("timestamp", -1))
