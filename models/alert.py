import datetime
import string


class Alert:
    def __init__(self, alert_id: string, product_id: string, threshold: float, active: bool, created_at: datetime, ID: string = None):
        self.alert_id = alert_id
        self.product_id = product_id
        self.threshold = threshold
        self.active = active
        self.created_at = created_at
        self.ID = ID
