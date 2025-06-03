from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.secretaria_schema import SecretariaPublic, SecretariaBase, SecretariaGet
from http import HTTPStatus

from app.controllers.secretaria_controller import (
    criar_secretaria,
    alterar_secretaria,
    apagar_secretaria,
    listar_secretarias,
    listar_secretarias_id
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SecretariaPublic, status_code=HTTPStatus.CREATED)
def criar(secretaria: SecretariaBase, db: Session = Depends(get_db)):
    return criar_secretaria(db, secretaria)

@router.get("/", response_model=list[SecretariaGet])
def listar(db: Session = Depends(get_db)):
    return listar_secretarias(db)

@router.get("/{secretaria_id}", response_model=SecretariaPublic)
def listar_por_id(secretaria_id: int, db: Session = Depends(get_db)):
    return listar_secretarias_id(db, secretaria_id)

@router.put("/{secretaria_id}", response_model=SecretariaPublic)
def alterar(secretaria_id: int, secretaria: SecretariaBase, db: Session = Depends(get_db)):
    return alterar_secretaria(db, secretaria_id, secretaria)

@router.delete("/{secretaria_id}", status_code=204)
def apagar(secretaria_id: int, db: Session = Depends(get_db)):
    apagar_secretaria(db, secretaria_id)
    return None
