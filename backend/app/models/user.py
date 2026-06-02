from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    full_name: Optional[str] = None
    phone: Optional[str] = None
    role: str = Field(default="customer")  # customer, admin, hall_owner
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    bookings: List["Booking"] = Relationship(back_populates="user")