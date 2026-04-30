from pydantic import BaseModel
from datetime import date
from typing import Optional

class WeightCreate(BaseModel):
    weight: float
    date: date
    calories: int
    
class WeightResponse(BaseModel):
    id: int
    weight: float
    date: date
    calories: int 
    
    class Config:
        from_attributes = True
        
class WeightUpdate(BaseModel):
    weight: Optional[float] = None
    calories: Optional[int] = None