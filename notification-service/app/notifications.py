import time
from app.models import Notification
from sqlalchemy.orm import Session

def send_notification(notification: Notification, db: Session):
    # Simulate sending
    print(f"Sending {notification.type} to user {notification.user_id}: {notification.message}")
    time.sleep(1)
    notification.status = "sent"
    db.commit()
