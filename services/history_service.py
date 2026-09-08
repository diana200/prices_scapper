from datetime import datetime

from models.offer_history import OfferHistory
from repositories.history_repo import add_history

def save_history(offer, product_id):
    entry = OfferHistory(
        offer_id=offer.offer_id,
        product_id=product_id,
        store=offer.store,
        price=offer.price,
        available=offer.available,
        timestamp=datetime.now()
    )
    add_history(entry)
