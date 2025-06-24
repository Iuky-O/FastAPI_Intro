from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.medico_schema import MedicoPublic, MedicoBase, MedicoGet
from http import HTTPStatus
from app.database.connection import SessionLocal

from app.controllers.medico_controller import (
        criar_medico,
        alterar_medico,
        apagar_medico,
        listar_medicos,
        listar_medicos_id
    )

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MedicoPublic, status_code=HTTPStatus.CREATED)
def criar(medico: MedicoBase, db: Session = Depends(get_db)):
    return criar_medico(db, medico)

@router.get("/", response_model=list[MedicoGet])
def listar(db: Session = Depends(get_db)):
    return listar_medicos(db)

@router.get("/{medico_id}", response_model=MedicoPublic)
def listar_por_id(medico_id: int, db: Session = Depends(get_db)):
    return listar_medicos_id(db, medico_id)

@router.put("/{medico_id}", response_model=MedicoPublic)
def alterar(medico_id: int, medico: MedicoBase, db: Session = Depends(get_db)):
    return alterar_medico(db, medico_id, medico)

@router.delete("/{medico_id}", status_code=204)
def apagar(medico_id: int, db: Session = Depends(get_db)):
    apagar_medico(db, medico_id)
    return None