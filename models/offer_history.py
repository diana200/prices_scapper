import datetime
import string


class OfferHistory:
    def __init__(self, offer_id: string, product_id: string, store: string, price: float, stock_status: string, timestamp: datetime, ID: string = None):
        self.offer_id = offer_id
        self.product_id = product_id
        self.store = store
        self.price = price
        self.stock_status = stock_status
        self.timestamp = timestamp
        self.ID = ID
