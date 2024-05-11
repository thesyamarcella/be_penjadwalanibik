from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ruangan(Base):
    __tablename__ = "ruangan"

    id = Column(Integer, primary_key=True, index=True)
    nama_ruangan = Column(String, index=True)
    kapasitas = Column(Integer)
    nama_gedung = Column(String)
    is_lab = Column(Boolean, default=False)

    def __repr__(self):
        return "Ruangan:  " + self.name

