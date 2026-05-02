from pydantic import BaseModel, Field
from datetime import date as DateType
from typing import Optional

class WeightCreate(BaseModel):
    weight: float = Field(ge=0)
    calories: int = Field(ge=0)
    date: Optional[DateType] = None

    
class WeightResponse(BaseModel):
    id: int
    weight: float
    date: DateType
    calories: int 
    
    class Config:
        from_attributes = True
        
class WeightUpdate(BaseModel):
    weight: Optional[float] = Field(default=None, ge=0)
    calories: Optional[int] = Field(default=None, ge=0)