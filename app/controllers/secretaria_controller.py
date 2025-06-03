from sqlalchemy.orm import Session, joinedload
from app.models.secretaria_model import Secretaria
from app.schemas.secretaria_schema import SecretariaCreate, SecretariaUpdate
from fastapi import HTTPException

def criar_secretaria(db: Session, secretaria: SecretariaCreate):
    nova_secretaria = Secretaria(**secretaria.dict())
    db.add(nova_secretaria)
    db.commit()
    db.refresh(nova_secretaria)
    return nova_secretaria

def listar_secretarias(db: Session):
    return db.query(Secretaria)\
        .options(joinedload(Secretaria.usuario))\
        .all()

def listar_secretarias_id(db: Session, secretaria_id: int):
    secretaria = db.query(Secretaria)\
        .options(joinedload(Secretaria.usuario))\
        .filter(Secretaria.secretaria_id == secretaria_id)\
        .first()
    
    if not secretaria:
        raise HTTPException(status_code=404, detail="Secretária não encontrada")
    return secretaria

def alterar_secretaria(db: Session, secretaria_id: int, dados: SecretariaUpdate):
    secretaria = db.query(Secretaria).filter(Secretaria.secretaria_id == secretaria_id).first()
    if not secretaria:
        raise HTTPException(status_code=404, detail="Secretária não encontrada")
    
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(secretaria, key, value)

    db.commit()
    db.refresh(secretaria)
    return secretaria

def apagar_secretaria(db: Session, secretaria_id: int):
    secretaria = db.query(Secretaria).filter(Secretaria.secretaria_id == secretaria_id).first()
    if not secretaria:
        raise HTTPException(status_code=404, detail="Secretária não encontrada")
    
    db.delete(secretaria)
    db.commit()
