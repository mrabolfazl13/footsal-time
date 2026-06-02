from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class Hall(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    capacity: int
    price_per_slot: float
    description: Optional[str] = None
    facilities: Optional[str] = None  # JSON string or separate table
    image_url: Optional[str] = None
    is_active: bool = True
    owner_id: int = Field(foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    timeslots: List["TimeSlot"] = Relationship(back_populates="hall")
    reviews: List["Review"] = Relationship(back_populates="hall")