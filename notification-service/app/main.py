from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import models, schemas, notifications
from rq import Queue
import redis

Base.metadata.create_all(bind=engine)
app = FastAPI()

redis_conn = redis.Redis(host="localhost", port=6379)
task_queue = Queue(connection=redis_conn)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notifications", response_model=schemas.NotificationOut)
def create_notification(notification_in: schemas.NotificationCreate, db: Session = Depends(get_db)):
    db_notification = models.Notification(**notification_in.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)

    # Queue the task
    task_queue.enqueue(notifications.send_notification, db_notification, db)
    return db_notification

@app.get("/users/{user_id}/notifications", response_model=list[schemas.NotificationOut])
def get_user_notifications(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
