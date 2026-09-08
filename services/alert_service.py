
import string
from repositories.alert_repo import get_alerts

def check_alerts(product_id: string, price: float):
    alerts = get_alerts(product_id)
    triggered = []

    for alert in alerts:
        if price <= alert["threshold"]:
            triggered.append(alert)

    return triggered
