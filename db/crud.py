from sqlalchemy.orm import Session
from fastapi import HTTPException
from db import models
from schemas import schemas
from datetime import date 

def create_entry(db: Session, entry: schemas.WeightCreate):
    
    # Normalize input: default missing date to today
    entry_data = entry.model_dump()
        
    if entry_data["date"] is None:
        entry_data["date"] = date.today()
        
    db_entry = models.WeightEntry(**entry_data)
    
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def get_entries(db: Session):
    return db.query(models.WeightEntry).order_by(models.WeightEntry.date).all()

def delete_entry(db: Session, entry_id: int):
    entry = db.query(models.WeightEntry).filter(models.WeightEntry.id == entry_id).first()
    
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    
    db.delete(entry)
    db.commit()
    
    return entry

def update_entry(db: Session, entry_id: int, entry_update):
    db_entry = db.query(models.WeightEntry).filter(models.WeightEntry.id == entry_id).first()

    if not db_entry:
        return None

    if entry_update.weight is not None:
        db_entry.weight = entry_update.weight

    if entry_update.calories is not None:
        db_entry.calories = entry_update.calories

    db.commit()
    db.refresh(db_entry)

    return db_entry