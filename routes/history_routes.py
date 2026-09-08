from flask import Blueprint, render_template

from repositories.history_repo import get_history
from repositories.product_repo import find_product_by_id

history_bp = Blueprint("history", __name__)

@history_bp.route("/products/<product_id>/offers/<offer_id>/history")
def history_page(product_id, offer_id):
    product = find_product_by_id(product_id)
    history = get_history(offer_id)
    return render_template("history.html", product=product, history=history)
