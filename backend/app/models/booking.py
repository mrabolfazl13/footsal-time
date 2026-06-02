from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    timeslot_id: int = Field(foreign_key="timeslot.id")
    status: str = "pending"  # pending, confirmed, cancelled
    booked_at: datetime = Field(default_factory=datetime.utcnow)
    
    user: "User" = Relationship(back_populates="bookings")
    timeslot: "TimeSlot" = Relationship(back_populates="booking")