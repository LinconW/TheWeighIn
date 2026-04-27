from sqlalchemy import Column, Integer, Float, Date
from .database import Base

class WeightEntry(Base):
    __tablename__ = "weight_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    calories = Column(Integer, nullable=False)
    