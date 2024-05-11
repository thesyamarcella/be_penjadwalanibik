from pydantic import BaseModel
from typing import List, Optional

class MataKuliahBase(BaseModel):
    kd_mata_kuliah: str
    nama_mata_kuliah: str
    tingkat_mata_kuliah: int
    id_program_studi: int
    semester: str
    is_lab: bool

class MataKuliahCreate(MataKuliahBase):
    pass

class MataKuliah(MataKuliahBase):
    id: int

    class Config:
        orm_mode = True

        
