""" Rotas Pacient """

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.paciente_schema import Pacient, PacientPublic, PacientUpdate, PacientOut
from http import HTTPStatus


from app.controllers.pacient_controller import (
    criar_paciente,
    listar_paciente,
    alterar_paciente,
    apagar_paciente,
    listar_paciente_by_id
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PacientOut, status_code=HTTPStatus.CREATED)
def criar_pacient(paciente: Pacient, db: Session = Depends(get_db)):
    """ Rota para criar Paciente """

    return criar_paciente(db, paciente)


@router.get("/", response_model=list[PacientOut])
def listar_pacient(db: Session = Depends(get_db)):
    """ Rota para listar Pacientes """

    return listar_paciente(db)


@router.get("/{paciente_id}", response_model=PacientPublic)
def listar_paciente_por_id(pacient_id: int, db: Session = Depends(get_db)):
    """ Função para listar Pacientes pelo id """

    return listar_paciente_by_id(db, pacient_id)


@router.put("/{pacient_id}", response_model=PacientPublic)
def alterar_pacient(pacient_id: int, paciente: PacientUpdate, db: Session = Depends(get_db)):
    """ Função para alterar Paciente"""

    return alterar_paciente(db, pacient_id, paciente)


@router.delete("/{pacient_id}", status_code=204)
def deletar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    """ Função para deletar Paciente """

    apagar_paciente(db, paciente_id)
    return None

