from sqlalchemy.orm import Session
from app.models.paciente_model import Paciente
from app.schemas.paciente_schema import Pacient, PacientUpdate
from fastapi import HTTPException


def criar_paciente(db: Session, paciente: Pacient):
    """ Função para criar Pacient """

    new_pacient = Paciente(**paciente.dict())
    db.add(new_pacient)
    db.commit()
    db.refresh(new_pacient)
    return new_pacient


def listar_paciente(db: Session):
    """ Função par listar Pacient """

    return db.query(Paciente).all()


def listar_paciente_by_id(db: Session, pacient_id: int):
    """ Função para listar Pacient pelo id """

    paciente = db.query(Paciente).filter(Paciente.paciente_id == pacient_id).first()

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")

    return paciente


def alterar_paciente(db: Session, pacient_id: int, dados: PacientUpdate):
    """ Função para alterar Pacient (Chamando Schema PacientUpdate)"""

    paciente = db.query(Paciente).filter(Paciente.paciente_id == pacient_id).first()

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")

    for key, value in dados.dict(exclude_unset=True).items():
        """ Setando dados do paciente atualizado com chave e valores.(dict)"""
        setattr(paciente, key, value)

    db.commit()
    db.refresh(paciente)
    return paciente


def apagar_paciente(db: Session, pacient_id: int):
    """ Função para apagar Paciente"""

    paciente = db.query(Paciente).filter(Paciente.paciente_id == pacient_id).first()

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado.")

    db.delete(paciente)
    db.commit()

