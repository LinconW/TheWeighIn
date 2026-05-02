
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import models, crud
from schemas import schemas
from db.database import Base, engine, SessionLocal

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "TheWeighIn API running"}

@app.post("/entries", response_model=schemas.WeightResponse)
def add_entry(entry: schemas.WeightCreate, db: Session = Depends(get_db)):
    return crud.create_entry(db, entry)

@app.get("/entries", response_model=list[schemas.WeightResponse])
def read_entries(db: Session = Depends(get_db)):
    return crud.get_entries(db)

@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    return crud.delete_entry(db, entry_id)

@app.patch("/entries/{entry_id}", response_model=schemas.WeightResponse)
def update_entry(
    entry_id: int,
    entry: schemas.WeightUpdate,
    db: Session = Depends(get_db)
):
    updated_entry = crud.update_entry(db, entry_id, entry)

    if not updated_entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    return updated_entry