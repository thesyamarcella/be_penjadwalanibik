from fastapi import FastAPI
from controllers import dosen, kelas, mata_kuliah, ruangan

app = FastAPI()
app.include_router(mata_kuliah.router, prefix="/mata_kuliah", tags=["Mata Kuliah"])
app.include_router(dosen.router, prefix="/dosen", tags=["Dosen"])
app.include_router(kelas.router, prefix="/kelas", tags=["Kelas"])
app.include_router(ruangan.router, prefix="/ruangan", tags=["Ruangan"])
