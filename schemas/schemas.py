from pydantic import BaseModel
from datetime import date

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