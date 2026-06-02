from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    hall_id: int = Field(foreign_key="hall.id")
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    user: "User" = Relationship()
    hall: "Hall" = Relationship(back_populates="reviews")