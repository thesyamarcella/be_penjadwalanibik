from fastapi import APIRouter, HTTPException
from models.jadwal import Jadwal
from services.jadwal import JadwalService

router = APIRouter()

@router.post("/", response_model=Jadwal)
async def create_jadwal(jadwal_data: Jadwal):
    return JadwalService.create_jadwal(jadwal_data.dict())

@router.get("/{jadwal_name}/", response_model=Jadwal)
async def get_jadwal(jadwal_name: str):
    jadwal = JadwalService.get_jadwal_by_name(jadwal_name)
    if jadwal is None:
        raise HTTPException(status_code=404, detail="Jadwal not found")
    return jadwal
