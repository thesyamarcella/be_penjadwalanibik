from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MataKuliah(Base):
    __tablename__ = "mata_kuliah"

    id = Column(Integer, primary_key=True, autoincrement=True)
    kd_mata_kuliah = Column(String, index=True)
    nama_mata_kuliah = Column(String, index=True)
    tingkat_mata_kuliah = Column(Integer)
    id_program_studi = Column(Integer)
    semester = Column(String)
    is_lab = Column(Boolean)

    def __repr__(self):
        return f"MataKuliah(id_mata_kuliah={self.id_mata_kuliah}, nama_mata_kuliah={self.nama_mata_kuliah})"
