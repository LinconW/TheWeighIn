from sqlalchemy import Column, Integer, Float, Date, String, DateTime
from datetime import datetime
from .database import Base

class WeightEntry(Base):
    __tablename__ = "weight_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    goal_phase = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    calories = Column(Integer, nullable=False)
    protein = Column(Integer, nullable=False)
    steps = Column(Integer, nullable=False)
    notes = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)