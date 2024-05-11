# schemas/kelas.py
from pydantic import BaseModel
from typing import List, Optional

class KelasBase(BaseModel):
    nama_kelas: str
    kuota: int
    shift: str = "pagi"

class KelasCreate(KelasBase):
    pass

class Kelas(KelasBase):
    id: int

    class Config:
        orm_mode = True
