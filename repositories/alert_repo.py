
import string
from db import db


def create_alert(alert):
    db.alerts.insert_one({
        "alert_id": alert.alert_id,
        "product_id": alert.product_id,
        "threshold": alert.threshold,
        "active": alert.active,
        "created_at": alert.created_at
    })

def get_alerts(product_id: string):
    query = {"product_id": product_id, "active": True}
    return list(db.alerts.find(query))

def disable_alert(alert_id: string):
    db.alerts.update_one({"alert_id": alert_id}, {"$set": {"active": False}})

def delete_alert(alert_id: string):
    db.alerts.delete_one({"alert_id": alert_id})
