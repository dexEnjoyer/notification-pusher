from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    message = Column(String)
    type = Column(String)  # email, sms, in-app
    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
