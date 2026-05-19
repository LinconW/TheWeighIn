from sqlalchemy import Column, Integer, Float, Date, String, DateTime
from datetime import datetime
from .database import Base

class WeightEntry(Base):
    __tablename__ = "weight_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    goal_phase = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    calories = Column(Integer, nullable=True)
    protein = Column(Integer, nullable=True)
    steps = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)