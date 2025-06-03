from fastapi import FastAPI, Depends
from app.database.create_db import create_tables
from app.database.connection import SessionLocal
from sqlalchemy import text
from app.views import usuario_view, medico_view, area_view, secretaria_view


app = FastAPI()

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

app.include_router(usuario_view.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(medico_view.router, prefix="/medicos", tags=["Médicos"])
app.include_router(secretaria_view.router, prefix="/secretaria", tags=["Secretárias"])
app.include_router(area_view.router, prefix="/areas", tags=["Áreas"])