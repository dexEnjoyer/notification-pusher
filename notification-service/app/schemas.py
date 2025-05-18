from pydantic import BaseModel
from typing import Literal

class NotificationCreate(BaseModel):
    user_id: int
    message: str
    type: Literal['email', 'sms', 'in-app']

class NotificationOut(BaseModel):
    id: int
    user_id: int
    message: str
    type: str
    status: str
    created_at: str

    class Config:
        orm_mode = True
