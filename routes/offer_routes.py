from flask import Blueprint, request, redirect

from services.product_service import upsert_offer

offer_bp = Blueprint("offers", __name__)

@offer_bp.route("/products/<product_id>/offers", methods=["POST"])
def add_offer_route(product_id):
    data = request.json
    product, offer = upsert_offer(data["name"], data)
    return {"status": "ok", "offer_id": offer.offer_id}
