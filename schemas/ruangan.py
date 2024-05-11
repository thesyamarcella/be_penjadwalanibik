from pydantic import BaseModel

class RuanganBase(BaseModel):
    nama_ruangan: str
    kapasitas: int
    nama_gedung: str
    is_lab: bool

class RuanganCreate(RuanganBase):
    pass

class Ruangan(RuanganBase):
    id: int

    class Config:
        orm_mode = True
