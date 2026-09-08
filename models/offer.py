import datetime
import string


class Offer:
    def __init__(self, offer_id: string, seller: string, seller_url: string, url: string, price: float, currency: string, stock_status: string, last_checked: datetime, ID: string = None):
        self.offer_id = offer_id
        self.seller = seller
        self.seller_url = seller_url
        self.url = url
        self.price = price
        self.currency = currency
        self.stock_status = stock_status
        self.last_checked = last_checked
        self.ID = ID
