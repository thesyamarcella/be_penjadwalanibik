from pydantic import BaseModel
from typing import List, Optional


class DosenBase(BaseModel):
    inisial: str
    gelar_depan: str
    nama_depan: str
    nama_belakang: str
    gelar_belakang: str

class DosenCreate(DosenBase):
    pass

class Dosen(DosenBase):
    id: int

    class Config:
        orm_mode = True
