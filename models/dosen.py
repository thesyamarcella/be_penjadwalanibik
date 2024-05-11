from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dosen(Base):
    __tablename__ = "dosen"

    id = Column(Integer, primary_key=True, index=True)
    inisial = Column(String)
    gelar_depan = Column(String)
    nama_depan = Column(String)
    nama_belakang = Column(String)
    gelar_belakang = Column(String)
    
    def __repr__(self):
        return "Dosen Pengampu: " + self.name
