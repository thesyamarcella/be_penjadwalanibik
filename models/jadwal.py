from pydantic import BaseModel

class Jadwal(BaseModel):
    start: str
    end: str
    day: str
    is_lab_slot: bool = False

    def __repr__(self):
        return "Pukul :" + self.start + "-" + self.end + " Hari: " + self.day
