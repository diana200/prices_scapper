# from db import products
import string
import datetime
import traceback
from datetime import datetime

from db import products
from models.offer import Offer
from models.product import Product


def find_product_by_id(product_id: string):
    p_id = str(product_id).lower()
    if product_id and len(p_id) > 0 and p_id != "null" and p_id != "none":
        return products.find_one({"pid": product_id})
    else:
        return None

def find_product_by_gpcid(product_gpcid: string):
    p_gpcid = str(product_gpcid).lower()
    if product_gpcid and len(p_gpcid) > 0 and p_gpcid != "null"  and p_gpcid != "none":
        return products.find_one({"gpcid": product_gpcid})
    else:
        return None

def find_product_by_name(name: string):
    if name and len(name) > 0:
        return products.find_one({"name": name})
    else:
        return None

def all_products():
    found_prods = products.find()
    return found_prods

def nr_products():
    found_prods = products.find()
    nr_products = len(list(found_prods))
    return nr_products

def create_product(product : Product):
    if product:
        found_product = find_product_by_id(product.pid)
        if not found_product:
            found_product = find_product_by_gpcid(product.gpcid)

        if not found_product:
            print("Product not found in repo -> save in databse")
            doc = {
                "pid": product.pid,
                "gpcid": product.gpcid,
                "name": product.name,
                "imgURL": product.imgURL,
                "created_at": datetime.now(),
                "offers": []
            }
            products.insert_one(doc)
            return True

    return False

def update_offer(product_data:object, offer: Offer):
    if product_data and offer:
        product_found = find_product_by_id(product_data["pid"])
        if not product_found:
            product_found = find_product_by_gpcid(product_data["gpcid"])

        if product_found:
            products.update_one(
                {
                    "pid": product_data["pid"],
                    "gpcid": product_data["gpcid"],
                    "offers.seller": offer.seller  # find product + offer by seller name
                },
                {
                    "$set": {
                        "offers.$.price": offer.price,
                        "offers.$.url": offer.url,
                        "offers.$.stock_status": offer.stock_status,
                        "offers.$.last_checked": offer.last_checked
                    }
                }
            )


def add_offer(product_data:object, offer: Offer):
    try:
        if product_data and offer:

            product_found = find_product_by_id(product_data["pid"])
            if not product_found:
                product_found = find_product_by_gpcid(product_data["gpcid"])

            if product_found:
                products.update_one(
                    {"pid": product_data["pid"], "gpcid": product_data["gpcid"]},  # filter
                    {"$push": {
                        "offers": {
                            "offer_id": offer.offer_id,
                            "seller": offer.seller,
                            "seller_url": offer.seller_url,
                            "url": offer.url,
                            "price": offer.price,
                            "currency": offer.currency,
                            "stock_status": offer.stock_status,
                            "last_checked": offer.last_checked
                        }
                    }}
                )
    except Exception as ex:
        print("Exception in add_offer: ", ex)
        traceback.print_exc()

