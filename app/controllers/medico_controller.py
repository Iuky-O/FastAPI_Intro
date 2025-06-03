from sqlalchemy.orm import Session, joinedload
from app.models.medico_model import Medico
from app.schemas.medico_schema import MedicoCreate, MedicoUpdate
from fastapi import HTTPException

def criar_medico(db: Session, medico: MedicoCreate):
    novo_medico = Medico(**medico.dict())
    db.add(novo_medico)
    db.commit()
    db.refresh(novo_medico)
    return novo_medico

def listar_medicos(db: Session):
    return db.query(Medico)\
        .options(joinedload(Medico.usuario), joinedload(Medico.area))\
        .all()

def listar_medicos_id(db: Session, medico_id: int):
    medico = db.query(Medico)\
        .options(joinedload(Medico.usuario), joinedload(Medico.area))\
        .filter(Medico.medico_id == medico_id)\
        .first()
    
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    return medico

def alterar_medico(db: Session, medico_id: int, dados: MedicoUpdate):
    medico = db.query(Medico).filter(Medico.medico_id == medico_id).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(medico, key, value)

    db.commit()
    db.refresh(medico)
    return medico

def apagar_medico(db: Session, medico_id: int):
    medico = db.query(Medico).filter(Medico.medico_id == medico_id).first()
    if not medico:
        raise HTTPException(status_code=404, detail="Médico não encontrado")
    
    db.delete(medico)
    db.commit()
