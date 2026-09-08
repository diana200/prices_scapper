from flask import Blueprint, request

from services.scraper_service import scrape
from services.product_service import upsert_offer
from services.history_service import save_history
from services.alert_service import check_alerts

scrape_bp = Blueprint("scrape", __name__)

@scrape_bp.route("/scrape", methods=["POST"])
def scrape_route():
    url = request.json["url"]

    scraped = scrape(url)
    product, offer = upsert_offer(scraped["name"], scraped)
    save_history(offer, product["product_id"])
    alerts = check_alerts(product["product_id"], offer.price)

    return {
        "product": product,
        "offer": offer.__dict__,
        "alerts_triggered": alerts
    }
