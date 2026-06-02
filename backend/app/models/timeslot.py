from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class TimeSlot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hall_id: int = Field(foreign_key="hall.id")
    start_time: datetime
    end_time: datetime  # 1.5 hours later
    price: float
    is_booked: bool = False
    hall: "Hall" = Relationship(back_populates="timeslots")
    booking: Optional["Booking"] = Relationship(back_populates="timeslot")