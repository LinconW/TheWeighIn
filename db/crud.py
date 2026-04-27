from sqlalchemy.orm import Session

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