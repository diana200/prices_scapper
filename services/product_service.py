from datetime import datetime
from bson import ObjectId
import traceback

from models.product import Product
from models.offer import Offer
from repositories.product_repo import (
    find_product_by_id,
    find_product_by_gpcid,
    update_offer,
    create_product,
    add_offer
)

def upsert_product(productData: object):

    product = None

    try:
        product = Product(
            pid=productData["pid"] if "pid" in productData else None,
            gpcid=productData["gpcid"] if "gpcid" in productData else None,
            name=productData["title"],
            imgURL=productData["image"],
            created_at=datetime.now(),
            offers=[]
        )

        db_product = find_product(product)

        if not db_product and product:
            create_product(product)
            db_product = find_product(product)

        saved_offers = upsert_offers(productData, db_product)
        product.offers = saved_offers

    except Exception as ex:
        print("exception in product_service.upsert_product: ", ex)
        traceback.print_exc()



    return product

def find_product(product:Product):
    db_product = find_product_by_id(product.pid)
    if not db_product:
        db_product = find_product_by_gpcid(product.gpcid)

    return db_product

def upsert_offers(product_data: object, db_product):
    saved_offers = []

    if product_data and db_product:
    # Fiecare produs are o listă de oferte
        if product_data and "offers" in product_data and len(product_data["offers"]) > 0:
            for offer in product_data["offers"]:
                if "seller" in offer:
                    # Salvează în MongoDB
                    saved_offer = upsert_offer(product_data, db_product, offer)
                    if saved_offer:
                        saved_offers.append(saved_offer)
    return saved_offers

def upsert_offer(product_data:object, db_product, offer_data: object):
    offer = None

    try:
        if product_data and db_product and offer_data:

            offer = Offer(
                offer_id=str(ObjectId()),
                seller=offer_data["seller"],
                seller_url=offer_data["seller_url"],
                url=offer_data["url"],
                price=offer_data["price"],
                currency=offer_data["currency"],
                stock_status=offer_data["stock_status"],
                last_checked=datetime.now()
            )

            selected_offers = [sel_offer for sel_offer in db_product["offers"] if sel_offer and "seller" in sel_offer and sel_offer["seller"] == offer_data["seller"]]
            existing = len(selected_offers) > 0

            if existing:
                # todo : create allert for offer with price below price threadshold
                offer.offer_id = selected_offers[0]["offer_id"]
                update_offer(product_data, offer)
                #existing = offer
            else:
                # todo : create allert for offer with price below price threadshold
                add_offer(product_data, offer)
    except Exception as ex:
        print("exception in product_service.upsert_offer: ", ex)
        traceback.print_exc()

    return offer
