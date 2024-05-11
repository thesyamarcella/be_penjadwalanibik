from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models.ruangan import Ruangan
from schemas.ruangan import RuanganCreate, Ruangan as RuanganSchema

router = APIRouter()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RuanganSchema)
async def create_ruangan(ruangan_data: RuanganCreate, db: Session = Depends(get_db)):
    db_ruangan = Ruangan(**ruangan_data.dict())
    db.add(db_ruangan)
    db.commit()
    db.refresh(db_ruangan)
    return db_ruangan

@router.get("/", response_model=List[RuanganSchema])
async def get_all_ruangan(db: Session = Depends(get_db)):
    return db.query(Ruangan).all()

# Similarly, you can implement other CRUD operations for Ruangan
