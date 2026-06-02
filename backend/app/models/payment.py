from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    booking_id: int = Field(foreign_key="booking.id")
    amount: float
    status: str = "pending"  # pending, paid, failed
    payment_method: Optional[str] = None
    transaction_id: Optional[str] = None
    paid_at: Optional[datetime] = None