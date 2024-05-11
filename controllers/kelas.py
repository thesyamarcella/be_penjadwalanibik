# controllers/kelas.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models.kelas import Kelas
from schemas.kelas import KelasCreate, Kelas as KelasSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=KelasSchema)
async def create_kelas(kelas_data: KelasCreate, db: Session = Depends(get_db)):
    db_kelas = Kelas(**kelas_data.dict())
    db.add(db_kelas)
    db.commit()
    db.refresh(db_kelas)
    return db_kelas

@router.get("/", response_model=List[KelasSchema])
async def get_all_kelas(db: Session = Depends(get_db)):
    return db.query(Kelas).all()
