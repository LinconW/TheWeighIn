from enum import Enum
from pydantic import BaseModel, Field
from datetime import date as DateType
from typing import Optional

class GoalPhase(str, Enum):
    cut = "cut"
    bulk = "bulk"
    maintenance = "maintenance"

class WeightCreate(BaseModel):
    goal_phase: GoalPhase
    weight: float = Field(ge=0)
    calories: Optional[int] = Field(default=None, ge=0)
    protein: Optional[int] = Field(default=None, ge=0)
    steps: Optional[int] = Field(default=None, ge=0)
    notes: Optional[str] = Field(default=None, max_length=500)
    date: Optional[DateType] = None

class WeightResponse(BaseModel):
    id: int
    goal_phase: GoalPhase
    weight: float
    calories: Optional[int] = Field(default=None, ge=0)
    protein: Optional[int] = Field(default=None, ge=0)
    steps: Optional[int] = Field(default=None, ge=0)
    notes: Optional[str] = Field(default=None, max_length=500)
    date: DateType
     
    class Config:
        from_attributes = True
        
class WeightUpdate(BaseModel):
    goal_phase: Optional[GoalPhase] = None
    weight: Optional[float] = Field(default=None, ge=0)
    calories: Optional[int] = Field(default=None, ge=0)
    protein: Optional[int] = Field(default=None, ge=0)
    steps: Optional[int] = Field(default=None, ge=0)
    notes: Optional[str] = Field(default=None, max_length=500)
    date: Optional[DateType] = None