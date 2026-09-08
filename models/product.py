import datetime
import string

from models import offer



class Product:

    def __init__(self, pid: string, gpcid: string, name: string, created_at: datetime, offers: list[offer.Offer], ID: string = None, imgURL: string = None):
        self.pid = pid
        self.gpcid = gpcid
        self.name = name
        self.imgURL = imgURL
        self.created_at = created_at
        self.offers = offers
        self.ID = ID
