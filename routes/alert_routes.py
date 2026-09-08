from flask import Blueprint, render_template, request, redirect

import datetime
from bson import ObjectId

from repositories.alert_repo import create_alert, disable_alert, delete_alert
from models.alert import Alert

alert_bp = Blueprint("alerts", __name__)

@alert_bp.route("/alerts/new")
def new_alert_page():
    product_id = request.args.get("product_id")
    product_name = request.args.get("product_name")
    return render_template("alert.html", product_id=product_id, product_name=product_name)


@alert_bp.route("/alerts", methods=["POST"])
def create_alert_route():
    alert = Alert(
        alert_id=str(ObjectId()),
        product_id=request.form["product_id"],
        threshold=float(request.form["threshold"]),
        active=True,
        created_at=datetime.datetime.now()
    )
    create_alert(alert)
    return redirect("/search")


@alert_bp.route("/alerts/<alert_id>/disable")
def disable_alert_route(alert_id):
    disable_alert(alert_id)
    return redirect("/search")


@alert_bp.route("/alerts/<alert_id>/delete")
def delete_alert_route(alert_id):
    delete_alert(alert_id)
    return redirect("/search")
