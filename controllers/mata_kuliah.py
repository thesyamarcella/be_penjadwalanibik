from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from database import SessionLocal
from models.mata_kuliah import MataKuliah
from schemas.mata_kuliah import MataKuliahCreate, MataKuliah as MataKuliahSchema

router = APIRouter()

# Function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MataKuliahSchema)
async def create_mata_kuliah(mata_kuliah_data: MataKuliahCreate, db: Session = Depends(get_db)):
    db_mata_kuliah = MataKuliah(**mata_kuliah_data.dict())
    db.add(db_mata_kuliah)
    db.commit()
    db.refresh(db_mata_kuliah)
    return db_mata_kuliah

@router.get("/", response_model=List[MataKuliahSchema])
async def get_all_mata_kuliah(db: Session = Depends(get_db)):
    return db.query(MataKuliah).all()

# Similarly, you can implement other CRUD operations for MataKuliah
