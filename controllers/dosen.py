from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models.dosen import Dosen
from schemas.dosen import DosenCreate, Dosen as DosenSchema

router = APIRouter()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DosenSchema)
async def create_dosen(dosen_data: DosenCreate, db: Session = Depends(get_db)):
    db_dosen = Dosen(**dosen_data.dict())
    db.add(db_dosen)
    db.commit()
    db.refresh(db_dosen)
    return db_dosen

@router.get("/", response_model=List[DosenSchema])
async def get_all_dosen(db: Session = Depends(get_db)):
    return db.query(Dosen).all()


