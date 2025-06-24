from fastapi import FastAPI, Depends
from app.database.create_db import create_tables
from app.database.connection import SessionLocal
from sqlalchemy import text
from fastapi.staticfiles import StaticFiles
from app.config import settings
import os
from app.views import upload_image_exame_view, usuario_view, medico_view, \
                     area_view, secretaria_view, pacient_view, imagem_exame_view, \
                     auth_view

app = FastAPI()

os.makedirs(settings.security.UPLOAD_DIR, exist_ok=True)
app.mount("/files", StaticFiles(directory=settings.security.UPLOAD_DIR), name="files")

def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()

@app.on_event("startup")
def startup():
   create_tables()

@app.get("/")
def read_root(db=Depends(get_db)):
   version = db.execute(text("SELECT version();")).fetchone()
   return {"PostgreSQL Version": version[0]}

app.include_router(auth_view.router, tags=["Login"])
app.include_router(usuario_view.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(medico_view.router, prefix="/medicos", tags=["Médicos"])
app.include_router(secretaria_view.router, prefix="/secretaria", tags=["Secretárias"])
app.include_router(area_view.router, prefix="/areas", tags=["Áreas"])
app.include_router(pacient_view.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(imagem_exame_view.router, prefix="/imagem/exame", tags=["Imagem Exame"])
app.include_router(upload_image_exame_view.router, prefix="/imagem/upload", tags=["Imagem Exame Upload"])