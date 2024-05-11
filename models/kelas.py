from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Kelas(Base):
    __tablename__ = "kelas"

    id = Column(Integer, primary_key=True, autoincrement=True,index =True)
    nama_kelas = Column(String, index=True)
    kuota = Column(Integer)
    shift = Column(String, default="pagi")
    
    def __repr__(self):
        return f"Kelas: {self.nama_kelas}, Shift: {self.shift}"
