from sqlalchemy.orm import Session
from fastapi import HTTPException
from db import models
from schemas import schemas

def create_entry(db: Session, entry: schemas.WeightCreate):
    db_entry = models.WeightEntry(**entry.model_dump())
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